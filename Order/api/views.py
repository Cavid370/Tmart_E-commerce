from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from Product.models import ProductVersionModel
from Order.models import Cart_item, CartModel, WishlistModel
from .serializers import (
                    CartItemSerializer,
                    CartSerializer,
                    ProductVersionSerializer,
                    WishlistSerializer,
                )
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
class ProductVersionAPI(ListAPIView):
    queryset = ProductVersionModel.objects.all()
    serializer_class = ProductVersionSerializer

class WishlistAPI(APIView):
    queryset = WishlistModel.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = WishlistModel.objects.filter(user_id = self.request.user).all()
        serializer = self.serializer_class(obj, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = ProductVersionModel.objects.filter(id=product_id).first()
        exist_wish_product = WishlistModel.objects.filter(user_id = request.user, product_version_id = product)
        if exist_wish_product.exists():
            print("bu userde artiq bu element wishlistdedir")
            message = {'success': True, 'message' : 'This product has already been added'}
            return Response(message, status = status.HTTP_302_FOUND)  
        else:
            if product:
                wishlist = WishlistModel(user_id = request.user, product_version_id = product)
                wishlist.save()
                message = {'success': True, 'message' : 'Product added to your wishlist.'}
                return Response(message, status = status.HTTP_201_CREATED)
            message = {'success' : False, 'message': 'Product not found.'}
            return Response(message, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            WishlistModel.objects.filter(user_id = self.request.user, product_version_id=ProductID).first().delete()
        return Response(status = status.HTTP_200_OK)


class BasketAPI(APIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        obj = CartModel.objects.filter(user_id = self.request.user, is_active = True).all()
        serializer = self.serializer_class(obj, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        quantity = request.data.get('quantity')
        product_id = request.data.get('product')
        product = ProductVersionModel.objects.filter(pk=product_id).first()
        exist_cart_product = Cart_item.objects.filter(user_id = request.user, product = product)
        if exist_cart_product.exists():     
            user_cart_item = Cart_item.objects.get(product = product_id, user_id = request.user)
            user_cart = CartModel.objects.get(cart_items=user_cart_item, user_id = request.user )
            user_cart.delete()
            user_cart_item.delete() 
            cart2 = Cart_item(user_id = request.user, product = product)
            cart2.quantity += int(quantity)
            cart2.total = quantity * cart2.product.product_id.new_price
            cart2.save()
            cart1 = CartModel(user_id = request.user, is_active = True,cart_items=cart2)
            cart1.save()      
            message = {'success': True, 'message' : 'The value has been changed because this product is already available'}
            return Response(message, status = status.HTTP_201_CREATED)  
        else:
            if product:
                cart2 = Cart_item(user_id = request.user, product = product)
                cart2.quantity += int(quantity)
                cart2.total = quantity * cart2.product.product_id.new_price
                cart2.save()
                cart1 = CartModel(user_id = request.user, is_active = True,cart_items=cart2)
                cart1.save()              
                message = {'success': True, 'message' : 'Product added to your card.'}
                return Response(message,status = status.HTTP_201_CREATED)
            message = {'success' : False, 'message': 'Product not found.'}
            return Response(message, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            user_cart_item = Cart_item.objects.get(product = ProductID, user_id = request.user)
            user_cart = CartModel.objects.get(cart_items=user_cart_item, user_id = request.user )
            user_cart.delete()
            user_cart_item.delete()
            message = {'success': True, 'message' : 'Product deleted'}
            return Response(message,status = status.HTTP_200_OK)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)
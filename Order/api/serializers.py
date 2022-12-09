from rest_framework import serializers

from Order.models import Cart_item, CartModel, WishlistModel
from Product.models import ProductVersionModel


class ProductVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVersionModel
        fields = [
            'product_id', 
        ]

class WishlistSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user_id.username')
    product_name= serializers.CharField(source='product_version_id.product_id.name')
    product_image = serializers.CharField(source='product_version_id.product_id.img')
    product_price = serializers.CharField(source='product_version_id.product_id.new_price')
    in_sale = serializers.CharField(source='product_version_id.product_id.in_sale')
    class Meta:
        model = WishlistModel
        fields = [
            'user_id',
            'product_name',
            'product_image',
            'product_price',
            'in_sale',
        ]

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartModel
        fields = [
            'user_id',
            'cart_items',
            'is_active'
        ]

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer()

    class Meta:
        model = Cart_item
        fields = ['user_id', 'product', 'quantity']

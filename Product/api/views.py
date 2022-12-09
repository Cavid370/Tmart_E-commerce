from django.conf import settings
from requests import request
from Product.models import ProductModel,Category
from rest_framework.views import APIView
from .serializers import *
from django.http import Http404
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated



class ProductView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            obj = self.get_object(pk)
            return Response(ProductSerializer(obj).data)

        product = ProductModel.objects.all()
        page_number = self.request.query_params.get('page', 1)
        if request.GET.get('category'):
            product = product.filter(category_id= request.GET.get('category'))
        if request.GET.get('tags'):
            product = product.filter(tags = request.GET.get('tags'))
        
        paginator = Paginator(product, settings.REST_FRAMEWORK['PAGE_SIZE'])
        serializer = ProductSerializer(paginator.page(page_number) , many=True)
        return Response(serializer.data)
    def get_object(self, pk):
        story_qs = ProductModel.objects.filter(id=pk)
        if story_qs.exists():
            return story_qs.first()
        raise Http404

    def post(self,request):
        new_product = CreateProductSerializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response(new_product.data)
        return Response(new_product.errors)

    def put(self, request, pk=None, *args, **kwargs):
        if pk:
            obj=self.get_object(pk)
        product_serializer = CreateProductSerializer(data= request.data,instance=obj)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(ProductSerializer(obj).data)
        return Response(product_serializer.errors)

    def patch(self, request,pk=None, *args, **kwargs):
        if pk:
            obj=self.get_object(pk)
        product_serializer = CreateProductSerializer(data=request.data,instance=obj,partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(ProductSerializer(obj).data)
        return Response(product_serializer.errors)

    def delete(self, request, pk=None, *args, **kwargs):
        if pk:
            product_qs = ProductModel.objects.filter(id=pk)
            if not product_qs.exists():
                raise Http404
            product=product_qs.first()
            product.delete()
            return Response(status=204) 

                
class CategoryView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            obj = self.get_object(pk)
            return Response(CategorySerializer(obj).data)
        category = Category.objects.all()
        page_number = self.request.query_params.get('page', 1)
        paginator = Paginator(category, settings.REST_FRAMEWORK['PAGE_SIZE'])
        serializer = CategorySerializer(paginator.page(page_number) , many=True)
        return Response(serializer.data)      
    def get_object(self, pk):
        category_qs = Category.objects.filter(id=pk)
        if category_qs.exists():
            return category_qs.first()
        raise Http404
    def post(self,request):
        new_category = CreateCategorySerializer(data = request.data)
        if new_category.is_valid():
            new_category.save()
            return Response(new_category.data)
        return Response(new_category.errors)
    def put(self,request,pk = None,*args,**kwargs):
        if pk:
            obj = self.get_object(pk)
        category = CreateCategorySerializer(data = request.data, instance = obj)
        if category.is_valid():
            category.save()
            return Response(CategorySerializer(obj).data)
        return Response(category.errors)
    def patch(self,request,pk = None,*args,**kwargs):
        if pk:
            obj = self.get_object(pk)
        category = CreateCategorySerializer(data = request.data, instance = obj, partial = True)
        if category.is_valid():
            category.save()
            return Response(CategorySerializer(obj).data)
        return Response(category.errors)
        
    def delete(self, request,pk, *args, **kwargs):
        category_qs = Category.objects.filter(id=pk)
        if not category_qs.exists():
            raise Http404
        category = category_qs.first()
        deleted_count, _= category.delete()
        # story.soft_delete()
        return Response(status=204)
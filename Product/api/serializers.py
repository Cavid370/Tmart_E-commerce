from rest_framework import serializers
from Product.models import ProductModel, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name')

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many= True)
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    detail_url = serializers.SerializerMethodField()
    def get_tags(self,obj):
        return [{'id': tag.id , 'name': tag.name} for tag in obj.tags.all()]

    def get_category(self,obj):
        return obj.category.category_name
    def get_detail_url(self,obj):
        return obj.get_absolute_url()
    class Meta:
        model = ProductModel   
        fields = ("id","name", "description", "img", 'img_s',"in_sale", 'category', 'tags','detail_url',"old_price","new_price",'slug')

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel   
        fields = ("name", "description", "img", 'img_s',"in_sale", 'category', 'tags')

 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')
        
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
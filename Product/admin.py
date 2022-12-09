from django.contrib import admin
from .models import Category, ProductModel, ProductVersionModel, ProductSizeModel, ProductColorModel, FeaturesModel, DataSheetModel, ReviewsModel,Tag,ProductStatistic
from modeltranslation.admin import TranslationAdmin

# Register your models here.

# class ProductAdmin(TranslationAdmin):
#     pass

# class CategoryAdmin(TranslationAdmin):
#     pass
# # class SubCategoryAdmin(TranslationAdmin):
# #     pass
# # admin.site.register(SubCategory, SubCategoryAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(ProductModel, ProductAdmin)
admin.site.register([Category,ProductModel,ProductVersionModel, ProductColorModel, ProductSizeModel, FeaturesModel, DataSheetModel, ReviewsModel,Tag,ProductStatistic])
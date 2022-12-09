from modeltranslation.translator import translator, TranslationOptions
from .models import ProductModel, Category

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(ProductModel, ProductTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)
translator.register(Category, CategoryTranslationOptions)


from modeltranslation.translator import TranslationOptions, register
from .models import Product

# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('title', 'slug', 'description',)
#     required_languages = ('en', 'tr',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','slug', 'description', 'content',)
    required_languages = ('en', 'tr',)

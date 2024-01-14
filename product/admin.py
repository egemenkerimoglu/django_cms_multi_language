from django.contrib import admin
from .models import  Product, ProductImage
# 3. part
from modeltranslation.admin import TranslationAdmin

# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(TranslationAdmin):
#     search_fields = ['title']
#     list_display = [
#         'id',
#         'title',
#         'title_en',
#         'slug',
#         'slug_en',
#         'is_activate',
#     ]
#     list_display_links = ['id', 'title']
#     prepopulated_fields = {
#         'slug': ['title'],
#     }

#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    search_fields = ['title']
    list_display = [
        'id',
        'title',
        'slug',
        'is_activate',
    ]
    list_display_links = ['id', 'title']
    prepopulated_fields = {
        'slug': ['title'],
    }
    inlines = [ProductImageAdmin]

    # class Meta:
    #     model = Product

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
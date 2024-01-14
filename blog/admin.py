from django.contrib import admin
from blog.models import BlogCategory, BlogTag, BlogPost
# 3. part
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslationAdmin):
    search_fields = ['title']
    list_display = [ 'title', 'slug', 'is_active']
    prepopulated_fields = { 'slug': ['title'], }

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = [ 'title', 'is_active']
    prepopulated_fields = {
        'slug': ['title'],
    }

@admin.register(BlogPost)
class BlogPostAdmin(TranslationAdmin):
    search_fields = ['title']
    list_display = [ 'title', 'slug', 'view_count', 'is_active', ]
    prepopulated_fields = { 'slug': ['title'], }

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

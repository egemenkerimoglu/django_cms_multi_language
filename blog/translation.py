from modeltranslation.translator import TranslationOptions, register
from .models import BlogPost, BlogCategory


@register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'description',)
    required_languages = ('en', 'tr',)

@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content',)
    required_languages = ('en', 'tr',)
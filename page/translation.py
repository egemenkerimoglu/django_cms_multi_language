from modeltranslation.translator import TranslationOptions, register

from page.models import Page

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ['title','slug','content']
    required_languages = ('en','tr')
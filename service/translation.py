from modeltranslation.translator import TranslationOptions, register

from service.models import Service

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ['title','slug', 'description', 'content']
    required_languages = ('en','tr')
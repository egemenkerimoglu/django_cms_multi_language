from django.contrib import admin
#3.party
from modeltranslation.admin import TranslationAdmin
from service.models import Service, ServiceImage

class ServiceImageAdmin(admin.StackedInline):
    model = ServiceImage

# Register your models here.
@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = [ 'id', 'title', 'title_en', 'is_activate']
    list_display_links = [ 'id', 'title']
    prepopulated_fields = { 
        'slug': ['title'],
        }
    inlines = [ServiceImageAdmin]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ServiceImage)
class PageImageAdmin(admin.ModelAdmin):
    pass
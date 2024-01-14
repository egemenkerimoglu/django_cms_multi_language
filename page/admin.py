from django.contrib import admin
#3.party
from modeltranslation.admin import TranslationAdmin
from page.models import Page, PageImage, ContactForm, CareerForm

@admin.register(CareerForm)
class CareerFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "subject", "created_at"]
    readonly_fields = ["name", "email", "subject", "phone", "created_at"]
    fieldsets = (
        ("BAŞVURULAR", {
            "fields": ("name", "email","phone","cv_files", "subject", "content", "created_at")
        }),
    )

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at"]
    readonly_fields = ["name", "email", "subject", "message", "created_at"]
    fieldsets = (
        ("MESAJLAR", {
            "fields": ("name", "email", "subject", "message", "created_at")
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return False


class PageImageAdmin(admin.StackedInline):
    model = PageImage

# Register your models here.
@admin.register(Page)
class PageAdmin(TranslationAdmin):
    list_display = [ 'id', 'title', 'title_en', 'is_activate']
    list_display_links = [ 'id', 'title']
    prepopulated_fields = { 
        'slug': ['title'],
        }
    inlines = [PageImageAdmin]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(PageImage)
class PageImageAdmin(admin.ModelAdmin):
    pass
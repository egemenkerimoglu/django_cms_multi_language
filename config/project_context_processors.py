# Global Olarak Değişten Eklemek ve Dağıtmak
from page.models import Page

def global_pages_context(request):
    return dict(
        # global_pages_context = Page.objects.values('id','title','slug').filter(is_activate=True)
        global_pages_context = Page.objects.filter(is_activate=True)
    )
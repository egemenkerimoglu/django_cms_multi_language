from django.urls import path
from page.views import single_page_view
app_name = 'page'

urlpatterns = [
    path('<slug:page_slug>', single_page_view, name='single_page_view' )
]
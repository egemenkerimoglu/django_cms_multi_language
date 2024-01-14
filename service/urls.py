from django.urls import path
from service.views import firs_service_view
app_name = 'service'

urlpatterns = [
    path('', firs_service_view, name='firs_service_view')
    # path('<slug:page_slug>', single_service_view, name='single_service_view' 
]
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include ,re_path
# Mulit Language
from django.utils.translation import gettext_lazy as _
# Media URL ve ROOT tanımı içim
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# My App
from page.views import home_page_view, contact_page_view, career_page_view

urlpatterns = [
    # Admin    
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    # Home Page
    path('', home_page_view, name='home_page_view'),
    
    # Contact Page
    path(_('iletisim/'), contact_page_view, name='contact_page_view'),
    path(_('kariyer/'), career_page_view, name='career_page_view'),
    # Page
    path('page/', include('page.urls', namespace='page')),

    # Service
    path('service/', include('service.urls', namespace='service')),

    # Product
    path('product/', include('product.urls', namespace='product')),

)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
]
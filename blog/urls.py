from django.urls import path

from .views import post_detail_view, all_posts_view

app_name = 'blog'

urlpatterns = [
    # Blog
    path('', all_posts_view, name='all_posts_view'),
    path('<slug:post_slug>', post_detail_view, name='post_detail_view'),
]

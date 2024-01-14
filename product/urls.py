from django.urls import path

from .views import product_detail_view, all_products_view

app_name = 'product'

urlpatterns = [
    # Product
    
    path('', all_products_view, name='all_products_view'),
    path('<slug:product_slug>', product_detail_view, name='product_detail_view'),
    # path('<slug:category_slug>', category_view, name='category_view'),
    # path('category/<slug:category_slug>/product/<int:id>/', product_detail_view, name='product_detail_view'),
    # path('', all_products_view, name='all_posts_view'),
    # path('<slug:post_slug>', post_detail_view, name='post_detail_view'),
]

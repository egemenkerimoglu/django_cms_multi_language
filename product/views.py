from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import  Product, ProductImage

# def category_view(request, category_slug):
#     #print(f"kategori slug : {category_slug}")
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(
#         is_activate=True,
#         category=category,
#     )
#     context = dict(
#         category=category,
#         products=products
#     )
#     return render(request, 'product/products_list.html', context)

def product_detail_view(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = dict(
        product=product
    )
    return render(request, 'product/detail.html', context)


# def product_detail_view(request, category_slug, id):
#     product = get_object_or_404(Product, category__slug=category_slug, pk=id)
#     product.view_count +=1
#     product.save()
#     product_images = ProductImage.objects.filter(product=product)
#     # randum 3 ürün listeleme
#     random_products = Product.objects.filter(
#         category=product.category
#     ).order_by('?')[:3]

#     context = dict(
#         random_products=random_products,
#         product=product,
#         product_images=product_images,
#     )
#     return render(request, 'product/detail.html', context)


def all_products_view(request):
    products = Product.objects.filter(is_activate=True)
    context = dict(
        products=products
    )
    return render(request, 'product/products_list.html', context)

# def all_category_view(request):
#     category = Category.objects.all
#     context = dict(
#         category=category
#     )
#     return render(request, 'product/products_list.html', context)
from django.db import models
from django.urls import reverse
# 3rd Party
#from autoslug import AutoSlugField
from tinymce import models as tinymce_models

# abstract model
class CommonModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    is_activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering  = ['-created_at']

# class Category(CommonModel):
#     parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
#     cover_image = models.ImageField(upload_to='product_category', blank=True)
#     description = models.CharField(max_length=160, blank=True)    

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         #aynı slug ile bir ebeveyn altında iki kategori olamayacağını zorlamak
#         # __str__ method elaborated later in post.  use __unicode__ in place of
#         unique_together = ('slug', 'parent',)    
#         verbose_name_plural = "categories"

class Product(CommonModel): # Book
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(upload_to='product', blank=True)
    description = models.CharField(max_length=160, blank=True)  
    content = tinymce_models.HTMLField(blank=True, null=True)    
    view_count = models.PositiveBigIntegerField(default=0)  

    def __str__(self):
        return self.title

    class Meta:
        ordering  = ['-created_at',]

    def get_absolute_url(self):
        return reverse(
            'product:product_detail_view',
            kwargs={
                "product_slug" : self.slug
            }
        )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)

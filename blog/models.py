from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Third Party Apps:
from tinymce import models as tinymce_models


# abstract model yapısı
class CommonModel(models.Model):
    title  = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)    

    class Meta:
        abstract = True
        ordering  = ['title'] # Default olarak title ayarla


class BlogCategory(CommonModel):
    description = models.TextField(blank=True, null=True)

    # admin listesinde isim gösermek için
    def __str__(self):
        return self.title

class BlogTag(CommonModel):    

    def __str__(self):
        return self.title
    

class BlogPost(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(BlogTag)    
    cover_image = models.ImageField(upload_to='post', blank=True, null=True) 
    description = models.CharField(max_length=160, blank=True)     
    content = tinymce_models.HTMLField(blank=True, null=True)    
    view_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
    
        
    class Meta:
        ordering  = ['-created_at',]

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail_view',
            kwargs={
                'post_slug': self.slug,
            }
        )
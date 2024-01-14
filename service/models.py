from django.db import models
from django.urls import reverse
# 3. Party
from tinymce import models as tinymce_models
# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    cover_image = models.ImageField(upload_to='service', blank=True, null=True) 
    description = models.CharField(max_length=160, blank=True)  
    content = tinymce_models.HTMLField(blank=True, null=True) 
    is_activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']

    def get_absolute_url(self):
        return reverse(
            'service:single_service_view',
            kwargs={
                "service_slug" : self.slug
            }
        )
    
class ServiceImage(models.Model):
    service = models.ForeignKey(Service, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='page', blank=True, null=True) 

    def __str__(self):
        return self.service.title   


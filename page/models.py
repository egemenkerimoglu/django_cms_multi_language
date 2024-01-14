from django.db import models
from django.urls import reverse
# 3. Party
from tinymce import models as tinymce_models
# Create your models here.

class CareerForm(models.Model):
    name = models.CharField("İsim Soyisim", max_length=150)
    email = models.EmailField("Email Adresi", max_length=150)
    phone = models.CharField("Email Adresi", max_length=150)
    date_of_birth = models.DateField("Doğum Tarihi")
    cv_file = models.FileField(upload_to='cv_files', blank=True)
    subject = models.CharField("Konu", max_length=300)
    content = models.TextField("Mesaj", max_length=2000)
    created_at = models.DateTimeField("Gönderilme Tarihi", auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Kariyer Mesajları"
        verbose_name = "Kariyer Mesajı"


class ContactForm(models.Model):
    name = models.CharField("İsim Soyisim", max_length=150)
    email = models.EmailField("Email Adresi", max_length=150)
    subject = models.CharField("Konu", max_length=300)
    message = models.TextField("Mesaj", max_length=2000)
    created_at = models.DateTimeField("Gönderilme Tarihi", auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "İletişim Mesajları"
        verbose_name = "İletişim Mesajı"


class Page(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(max_length=200, unique=True, null=False)
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
            'page:single_page_view',
            kwargs={
                "page_slug" : self.slug
            }
        )
    
class PageImage(models.Model):
    page = models.ForeignKey(Page, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='page', blank=True, null=True) 

    def __str__(self):
        return self.page.title   


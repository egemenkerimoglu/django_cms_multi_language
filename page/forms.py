from django import forms
from django.core.mail import send_mail

class CareerForm(forms.Form):
    name = forms.CharField(label='İsim Soyisim', max_length=200, min_length=2)
    email = forms.EmailField(label='E-Posta')
    phone = forms.CharField(label='Telefon')
    date_of_birth = forms.DateField()
    cv_file  = forms.FileField(label='CV Yükleyin')
    content = forms.CharField(label='Mesajınız', widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))
    kvkk = forms.CheckboxInput()

class ContactForm(forms.Form):
    name = forms.CharField(label='İsim Soyisim', max_length=200, min_length=2)
    email = forms.EmailField(label='E-Posta')
    content = forms.CharField(label='Mesajınız', widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))
    kvkk = forms.CheckboxInput()

    def send_email(self, content):
        
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var',            
            message=content,
            # None olursa DEFAULT_FROM_EMAIL daki emaile gönderir
            from_email=None,            
            recipient_list=['egemen@elkomyazilim.com'],
            # Mail gönderiminde hata olursa bildirim 
            fail_silently=False
        )
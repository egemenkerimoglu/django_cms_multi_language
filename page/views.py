from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from page.models import Page, PageImage
from page.forms import ContactForm, CareerForm
from django.contrib import messages

from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def home_page_view(request):
    context = dict()
    return render(request, 'page/home_page.html', context)

def career_page_view(request):
    if request.method == 'POST':
        form = CareerForm(request.POST or None)        
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            html = render_to_string('page/components/email.html', {
                'name': name,
                'email':email,
                'content':content
            })
            #print(email)
            send_mail(
                "İletişim Formu",
                "Form Mesajı",
                "info@ares.com.tr",
                ["egemen@elkoymazilim.com"],
                html_message=html
            )
            messages.success(request, "Kariyer formunuz iletildi.")
            return redirect('career_page_view')  
        else:
            messages.warning(request, form.errors)
            return redirect('career_page_view')
    form=CareerForm()
    context = dict(
        form=form
    )
    return render(request, 'page/career.html', context)


def contact_page_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)        
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            html = render_to_string('page/components/email.html', {
                'name': name,
                'email':email,
                'content':content
            })
            #print(email)
            send_mail(
                "İletişim Formu",
                "Form Mesajı",
                "info@ares.com.tr",
                ["egemen@elkoymazilim.com"],
                html_message=html
            )
            # form.send_emails(
            #     content=form.cleaned_data.get('content')
            # )
            messages.success(request, "İletişim formunuz iletildi.")
            return redirect('contact_page_view')  
        else:
            messages.warning(request, form.errors)
            return redirect('contact_page_view')
    form=ContactForm()
    context = dict(
        form=form
    )
    return render(request, 'page/contact_page.html', context)


def single_page_view(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    page_images= PageImage.objects.filter(page=page)
    context = dict(
        page=page,
        page_images=page_images
    )
    return render(request, 'page/single_page.html',context)


from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from service.models import Service


# Create your views here.
def firs_service_view(request):
    service = Service.objects.first()
    context = dict(
        service=service
    )
    return render(request, 'service/single_service.html', context)

# def single_service_view(request, service_slug):
#     service = get_object_or_404(Service, slug=service_slug)
#     #page_images= PageImage.objects.filter(page=page)
#     context = dict(
#         service=service,
#         #page_images=page_images
#     )
#     return render(request, 'service/single_service.html',context)


from django.shortcuts import render
import contacts.models as contacts
import site_settings.models as settings
from .models import *


def objects(request):
    data = {
        'meta': MetaTags.objects.all(),
        'objects': Objects.objects.all(),
        'objects_images': ObjectImages.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'objects',
        'phones': contacts.PhoneNumbers.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    return render(request, 'objects/index.html', context=data)

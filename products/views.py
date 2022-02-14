from django.shortcuts import render
import contacts.models as contacts
import site_settings.models as settings
from .models import *


def products(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'products',
        'products': Products.objects.all(),
        'phones': contacts.PhoneNumbers.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    print(data['products'])
    return render(request, 'products/index.html', context=data)

from django.shortcuts import render
import contacts.models as contacts
import products.models as products
import site_settings.models as settings
from .models import *


def product(request, slug):
    data = {
        'slug': slug,
        'products': products.Products.objects.all(),
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'product',
        'phones': contacts.PhoneNumbers.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    return render(request, 'product/index.html', context=data)

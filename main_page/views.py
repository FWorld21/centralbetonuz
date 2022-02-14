from django.shortcuts import render
import contacts.models as contacts
import products.models as products
import site_settings.models as settings
from .models import *


def home(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'home',
        'banners': Banners.objects.all(),
        'partners': WorkingWithUs.objects.all(),
        'news': News.objects.all(),
        'products': products.Products.objects.all(),
        'phones': contacts.PhoneNumbers.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    return render(request, 'main_page/index.html', context=data)

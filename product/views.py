from django.shortcuts import render
import contacts.models as contacts
import products.models as products
import site_settings.models as settings
from .models import *
import os


def product(request, slug):
    contact_info = {
        'name': request.GET.get('name'),
        'phone': request.GET.get('phone'),
        'email': request.GET.get('email'),
    }
    data = {
        'success_sent': False,
        'slug': slug,
        'products': products.Products.objects.all(),
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'product',
        'phones': contacts.PhoneNumbers.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    if contact_info['name'] or contact_info['phone'] or contact_info['email']:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--email "{contact_info["email"]}"')
        data['success_sent'] = True

    return render(request, 'product/index.html', context=data)

from django.shortcuts import render
import contacts.models as contacts
import site_settings.models as settings
from .models import *


def about(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'about',
        'phones': contacts.PhoneNumbers.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    return render(request, 'about/index.html', context=data)

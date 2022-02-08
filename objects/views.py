from django.shortcuts import render
import contacts.models as contacts
import site_settings.models as settings
from .models import *


def objects(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'about',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    return render(request, 'objects/index.html', context=data)

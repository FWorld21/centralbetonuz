from django.shortcuts import render
import contacts.models as contacts
import site_settings.models as settings
from .models import *


def contacts(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'contacts',
        'phones': PhoneNumbers.objects.all(),
        'addresses': Addresses.objects.all(),
    }
    return render(request, 'contacts/index.html', context=data)

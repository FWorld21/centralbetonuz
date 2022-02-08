from django.shortcuts import render
import contacts.models as contacts
import site_settings.models as settings
from .models import *


def home(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'page': 'home',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    return render(request, 'main_page/index.html', context=data)
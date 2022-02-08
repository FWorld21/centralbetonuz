from django.urls import path
from . import views

urlpatterns = [
    path('', views.objects, name='objects'),
]

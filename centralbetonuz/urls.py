from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('main_page.urls'), name='home'),
    path('products/', include('products.urls'), name='products'),
    path('product/', include('product.urls'), name='product'),
    path('objects/', include('objects.urls'), name='objects'),
    path('contacts/', include('contacts.urls'), name='contacts'),
    path('about/', include('about.urls'), name='about'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


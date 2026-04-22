from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

   
    path('', include('main.urls')),
    path('value/', include('value.urls')),
    path('about/', include('about.urls')),
    path('classes/', include('classes.urls')),
    path('contact/', include('contact.urls')),
    path('regulation/', include('regulation.urls')),
    path('team/', include('team.urls')),
    path('products/', include('product.urls')),
    path('franchise/', include('franchise.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# haha_art/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls')),
    path('value/', include('value.urls')),
    path('about/', include('about.urls')),
    path('classes/', include('classes.urls', namespace='classes')),  # ← thêm namespace
    path('contact/', include('contact.urls')),
    path('regulation/', include('regulation.urls')),
    path('team/', include('team.urls')),
    path('products/', include('product.urls')),
    path('franchise/', include('franchise.urls')),
    path('news/', include('new.urls')),  # Thêm đường dẫn cho ứng dụng news
    path('brand-story/', include('brand_story.urls')),
    path('policy/', include('policy.urls')),  # Thêm đường dẫn cho ứng dụng policy

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
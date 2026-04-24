from django.urls import path
from . import views

app_name = 'brand_story'

urlpatterns = [
    path('', views.brand_story, name='brand_story'),
]
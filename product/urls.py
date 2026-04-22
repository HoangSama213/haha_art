from django.urls import include, path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    
]
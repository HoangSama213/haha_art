# classes/urls.py
from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]
from django.urls import path
from . import views

app_name = 'regulation'

urlpatterns = [
    path('', views.index, name='classregulation'),
]
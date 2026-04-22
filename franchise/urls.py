from django.urls import path
from . import views

app_name = 'franchise'

urlpatterns = [
    path('', views.index, name='franchise'),
]
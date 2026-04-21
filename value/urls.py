from django.urls import path
from . import views

app_name = 'value'

urlpatterns = [
    path('', views.index, name='valueclassroom'),
]
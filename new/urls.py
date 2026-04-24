from django.urls import include, path
from . import views

app_name = 'new'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:news_id>/', views.detail, name='detail'),
]
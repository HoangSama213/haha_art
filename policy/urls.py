from django.urls import path
from . import views

app_name = 'policy'

urlpatterns = [
    path('term_of_use/', views.service, name='service'),
    path('refund/', views.refund, name='refund'),
    path('privacy/', views.privacy, name='privacy'),
    path('payment/', views.payment, name='payment'),
]
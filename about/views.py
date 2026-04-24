from django.shortcuts import render

from product.models import Product
from team.models import Teacher
from .models import *
from regulation.models import *

def index(request):
    about = AboutSection.objects.first()
    policy = TrainingPolicy.objects.first()
    teacher = Teacher.objects.all()
    products = Product.objects.all()
    different = Different.objects.first()
    context = {
        'page_title': 'About Us',
        'about': about,
        'policy':policy,
        'teacher': teacher,
        'products': products,
        'different': different,
    }
    return render(request, 'about/aboutus.html', context)

def introduce(request):
    about = AboutSection.objects.first()
    context = {
        'page_title': 'Introduce',
        'about': about,
    }
    return render(request, 'about/introduce.html', context)

def different(request):
    different = Different.objects.first()
    context = {
        'page_title': 'Điểm khác biệt',
        'different': different,
    }
    return render(request, 'about/different.html', context)
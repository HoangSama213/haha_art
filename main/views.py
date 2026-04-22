from django.shortcuts import render

from classes.models import Classes
from product.models import Product
from team.models import Teacher
from regulation.models import *
from about.models import *





def index(request):
    about = AboutSection.objects.first()
    policy = TrainingPolicy.objects.first()
    products = Product.objects.all()
    teacher = Teacher.objects.all()
    classes = Classes.objects.all()
    # ... các context khác
    context = {
        'about': about,
        'policy': policy,
        'products': products,
        'teacher': teacher,
        'classes': classes,

        # ...
    }
    return render(request, 'main/index.html', context)
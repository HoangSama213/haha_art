from django.shortcuts import render

from classes.models import Classes
from product.models import Product
from team.models import Teacher
from regulation.models import *
from about.models import *




from .models import Carousel

def index(request):
    carousels = Carousel.objects.all()  # ✅ thêm lại dòng này

    about = AboutSection.objects.first()
    policy = TrainingPolicy.objects.first()
    products = Product.objects.all()
    teacher = Teacher.objects.all()
    classes = Classes.objects.all()

    context = {
        'carousels': carousels,  # ✅ QUAN TRỌNG
        'about': about,
        'policy': policy,
        'products': products,
        'teacher': teacher,
        'classes': classes,
    }

    return render(request, 'main/index.html', context)


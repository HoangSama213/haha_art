from django.shortcuts import render
from .models import AboutSection, TrainingPolicy

def index(request):
    """Trang chủ"""
    context = {

    }
    return render(request, 'main/index.html', context)



def index(request):
    about = AboutSection.objects.first()
    policy = TrainingPolicy.objects.first()
    # ... các context khác
    context = {
        'about': about,
        'policy': policy,
        # ...
    }
    return render(request, 'main/index.html', context)
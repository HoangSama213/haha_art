from django.shortcuts import render

from regulation.models import TrainingPolicy


def index(request):
    policy = TrainingPolicy.objects.first()
    context = {
        'page_title': 'Quy chế',
        'policy': policy,
    }
    return render(request, 'regulation/classregulation.html', context)

def regulation(request):
    policy = TrainingPolicy.objects.first()
    context = {
        'page_title': 'Regulation',
        'policy': policy,
    }
    return render(request, 'regulation/regulation.html', context)
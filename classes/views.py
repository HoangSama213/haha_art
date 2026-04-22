from django.shortcuts import render

from classes.models import Classes


def index(request):
    classes = Classes.objects.all()
    context = {
        'page_title': 'Khóa học',
        'classes': classes,
    }
    return render(request, 'classes/classes.html', context)
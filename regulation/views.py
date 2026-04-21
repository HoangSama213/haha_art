from django.shortcuts import render


def index(request):
    return render(request, 'regulation/classregulation.html')
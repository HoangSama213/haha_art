from django.shortcuts import render
from .models import *

def index(request):
    teacher = Teacher.objects.all()
    context = {
        'page_title': 'Đội ngũ giáo viên',
        'teacher': teacher,
    }
    return render(request, 'team/team.html', context)
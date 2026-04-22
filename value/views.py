from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'Giá trị',
    }
    return render(request, 'value/valueclassroom.html', context)
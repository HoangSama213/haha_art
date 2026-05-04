from django.shortcuts import render

# Create your views here.
def service(request):
    context = {
        'page_title': 'Điều khoản sử dụng',
    }
    return render(request, 'policy/service.html', context)

def refund(request):
    context = {
        'page_title': 'Chính sách hoàn trả',
    }
    return render(request, 'policy/refund.html', context)

def privacy(request):
    context = {
        'page_title': 'Chính sách bảo mật',
    }
    return render(request, 'policy/privacy.html', context)

def payment(request):
    context = {
        'page_title': 'Chính sách thanh toán',
    }
    return render(request, 'policy/payment.html', context)
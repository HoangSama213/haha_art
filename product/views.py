from django.shortcuts import render

from product.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'page_title': 'Tác phẩm',
        'products': products,
    }
    return render(request, 'products/product.html', context)
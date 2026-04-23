# main/context_processors.py
from product.models import Product

def footer_products(request):
    return {
        'products': Product.objects.all()[:3]
    }
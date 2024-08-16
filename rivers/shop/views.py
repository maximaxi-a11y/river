from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Получение товара по его ID
    return render(request, 'product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.prefetch_related('images').all()
    return render(request, 'product_list.html', {'products': products})


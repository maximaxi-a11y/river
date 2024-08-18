from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Получение товара по его ID
    return render(request, 'shop/dt.html', {'product': product})

def product_list(request):
    products = Product.objects.prefetch_related('images').all()
    return render(request, 'shop/tt.html', {'products': products})


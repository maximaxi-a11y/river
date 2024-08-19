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


def cart_detail(request,):
    cart = Cart(request)
    total_price = cart.get_total_price()

    for key, value in request.POST.items():
            if key.startswith('quantity_'):
                product_id = key.split('_')[1]
                try:
                    quantity = int(value)
                    if quantity > 0:
                        cart.add(product_id=product_id, quantity=quantity, update_quantity=True)
                    else:
                        cart.remove(product_id=product_id)
                except ValueError:
                    continue


    for item in cart:
        product = item['product']
        first_image = product.images.first()  # Получение первого изображения
        item['image'] = first_image.image.url if first_image else None 
    return render(request, 'cart/detail.html', {'cart': cart, 'total_price': total_price})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Получение товара по его ID
    cart_add_product_form = CartAddProductForm()
    return render(request, 'shop/dt.html', {'product': product,'cart_add_product_form': cart_add_product_form})

def product_list(request):
    products = Product.objects.prefetch_related('images').all()
    return render(request, 'shop/tt.html', {'products': products})


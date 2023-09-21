from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart
from inventario.models import Producto

def cart(request):
    cart = get_or_create_cart(request)

        
    return render(request, 'carts/cart.html', {
        'cart':cart
    })
    
def add(request):
    cart = get_or_create_cart(request)
    product = Producto.objects.get(pk=request.POST.get('producto_id'))
    
    cart.products.add(product)
    return render(request, 'carts/add.html', {
        'product': product
    })
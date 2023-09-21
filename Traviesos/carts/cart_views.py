from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart
from inventario.models import Producto

def cart(request):
    cart = get_or_create_cart(request)

        
    return render(request, 'carts/cart.html', {
        
    })
    
def add(request):
    cart = get_or_create_cart(request)
    products = Producto.objects.get(id=request.POST.get('product_id'))
    
    return render(request, 'carts/add.html', {
        'product': Producto
    })
from django.shortcuts import render
from .models import Cart
from . utils import get_or_create_cart

def cart(request):
    cart = get_or_create_cart(request)

        
    return render(request, 'carts/cart.html', {
        
    })
    
def add(request):
    cart = get_or_create_cart(request)
    producto = product.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.add(producto)
    
    return render(request, 'carts/add.html', {
        'product': producto
    })
from django.urls import path
from . import cart_views

app_name = 'carts'

urlpatterns = [
    path('', cart_views.cart, name='cart'),
    path('', cart_views.add, name='add'),
]

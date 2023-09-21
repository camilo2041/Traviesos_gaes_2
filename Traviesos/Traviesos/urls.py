from django.contrib import admin
from django.urls import path
from landing import views
from django.urls import include
from gestion_citas import citas_views
from PQRS import pqrs_views
from carts import cart_views
from PQRS import pqrs_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('carrito/', include('carts.urls')),
    path('add/', cart_views.add, name='add'),
    path('juguetes/', views.juguetes, name='juguetes'),
    path('camas_muebles/', views.camas_muebles, name='camas_muebles'),
    path('ropas_accesorios/', views.ropas_accesorios, name='ropas_accesorios'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('citas', citas_views.formulario_agendar, name='citas'),
    path('pqrs', pqrs_views.pqrs, name='pqrs'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('datos', views.registro_informacion_adicional, name='datos'),
    path('citas/mascotas', citas_views.agregar_mascota, name='mascota'),
    path('citas/lista_citas', citas_views.ver_citas, name='lista_citas'),
    path('citas/datos_mascotas', citas_views.datos_mascota, name='datos_mascota'),
    path('comentarios', pqrs_views.coment, name='coment'),
    path('peril pqrs/', pqrs_views.lista_pqrs, name='lista_pqrs')
]

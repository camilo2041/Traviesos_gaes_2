from django.contrib import admin
from django.urls import path, include
from landing import views
from gestion_citas import citas_views
from PQRS import pqrs_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('carrito/', include('carts.urls')),
    path('juguetes/', views.juguetes, name='juguetes'),
    path('camas_muebles/', views.camas_muebles, name='camas_muebles'),
    path('ropas_accesorios/', views.ropas_accesorios, name='ropas_accesorios'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('Agendar', citas_views.formulario_agendar, name='citas'),
    path('perfil/citas/mascotas/datos_mascotas', citas_views.datos_mascota, name='datos_mascotas'),
    path('perfil/citas/mascotas/', citas_views.agregar_mascota, name='agregar_mascotas'),
    path('perfil/citas/mascotas/citas/lista_citas', citas_views.ver_citas, name='ver_citas'),
    path('eliminar_mascota/<int:mascota_id>/',citas_views.eliminar_mascota, name='eliminar_mascota'),
    path('pqrs/', pqrs_views.pqrs, name='pqrs'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('datos/', views.registro_informacion_adicional, name='datos'),
    path('comentarios/', pqrs_views.coment, name='coment'),
]

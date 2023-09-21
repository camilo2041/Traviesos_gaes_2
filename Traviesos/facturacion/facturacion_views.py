from django.shortcuts import render, redirect 
from inventario.models import Producto, DetalleCompra


def comprar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    
    if request.method == "POST":
        # Obtener la cantidad ingresada por el usuario desde el formulario
        cantidad_comprada = int(request.POST.get("cantidad", 0))
        
        # Verificar si la cantidad disponible es suficiente
        if cantidad_comprada > 0 and cantidad_comprada <= producto.cantidad_disponible:
            # Realizar la compra descontando la cantidad de la base de datos
            producto.cantidad_disponible -= cantidad_comprada
            producto.save()
            
            # Crear un objeto DetalleCompra y agregarlo a la compra actual
            detalle_compra = DetalleCompra(Id_producto=producto, cantidad=cantidad_comprada)
            detalle_compra.save()
            
            # Redirige a una página de confirmación de compra
            return redirect("pagina_de_confirmacion")  # Ajusta esto según tu configuración
        else:
            mensaje_error = "La cantidad ingresada no es válida o no hay suficientes unidades disponibles."
            return render(request, "compras/error.html", {"mensaje_error": mensaje_error})
    
    return render(request, "compras/comprar.html", {"producto": producto})

def confirmacion (request):
    return render (request, 'compras/confirmacion.html')
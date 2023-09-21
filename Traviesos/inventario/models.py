from django.db import models

class Marca(models.Model):
    Nombre_marca = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre_marca
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'marcas'
        ordering = ['id']

class Categoria(models.Model):
    Nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre_categoria
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categorias'
        ordering = ['id'] 
        
class Producto(models.Model):
    Nombre_producto = models.CharField(max_length=30)
    Precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    Imagen_producto = models.CharField(max_length=100)
    Descripcion_producto = models.CharField(max_length=50)
    Id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad_disponible = models.CharField(max_length=300, default=1)

    def __str__(self):
        return self.Nombre_producto
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['id']

class DetalleCompra(models.Model):
    Id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)  # Cantidad de productos comprados en esta compra

    def __str__(self):
        return f"{self.cantidad} de {self.Id_producto.Nombre_producto}"

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'
        db_table = 'detalles_compra'
        ordering = ['id']        
        
class Compras(models.Model):
    Nombre_compra = models.CharField(max_length=30)
    detalles = models.ManyToManyField(DetalleCompra)  # Nueva relación

    def __str__(self):
        return self.Nombre_compra

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'compras'
        ordering = ['id']

class Proveedor(models.Model):
    Nombre_proveedor = models.CharField(max_length=30)
    Apellido_proveedor = models.CharField(max_length=30)
    Telefono_Proveedor = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_proveedor
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedores'
        ordering = ['id']
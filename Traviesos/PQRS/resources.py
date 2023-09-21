from import_export import resources
from .models import PQRS, Estado  

class PqrsResource(resources.ModelResource):
    class Meta:
        model = PQRS  
        fields = ('id', 'Tipo_pqrs', 'usuario', 'Descripcion', 'Respuesta', 'Estado_pqrs')

class EstadoResource(resources.ModelResource):
    class Meta:
        model = Estado
        fields = ('id', 'Estado_pqrs')

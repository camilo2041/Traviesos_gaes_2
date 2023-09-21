from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PQRS, Estado
from .resources import EstadoResource

@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin):
    resource_class = EstadoResource

@admin.register(PQRS)
class PQRSAdmin(admin.ModelAdmin):
    list_display = ('Tipo_pqrs', 'usuario', 'Descripcion', 'Respuesta', 'Estado_pqrs')
    list_editable = ('Respuesta',)
    search_fields = ('create_at',)
    list_filter = ('Tipo_pqrs',)
    list_per_page = 10

    def formatted_create_at(self, obj):
        return obj.create_at.strftime("%Y-%m-%d %H:%M:%S")
    formatted_create_at.short_description = 'Fecha de Creación'


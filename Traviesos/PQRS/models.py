from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    Estado_pqrs = models.CharField(max_length=30)

    def __str__(self):
        return self.Estado_pqrs

class PQRS(models.Model):
    TIPO_PQRS_CHOICES = [
        ('Seleccionar', 'Seleccionar'),
        ('Peticion', 'Peticion'),
        ('Queja', 'Queja'),
        ('Reclamo', 'Reclamo'),
        ('Sugerencia', 'Sugerencia'),
    ]

    Tipo_pqrs = models.CharField(max_length=100, choices=TIPO_PQRS_CHOICES, verbose_name='Tipo pqrs')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    Descripcion = models.TextField(max_length=500, verbose_name='Descripcion', default='')
    Respuesta = models.CharField(max_length=150, blank=True, null=True)
    Estado_pqrs = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    
def __str__(self):
        return self.Descripcion

# Esta función se ejecutará después de que se guarde una instancia de PQRS
@receiver(post_save, sender=PQRS)
def actualizar_estado(sender, instance, **kwargs):
    if instance.Respuesta and instance.Estado_pqrs.Estado_pqrs == "Pendiente":
        estado_respuesta = Estado.objects.get(Estado_pqrs="En proceso")
        instance.Estado_pqrs = estado_respuesta
        instance.save()
    
    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS´s'
        db_table = 'pqrs'
        ordering = ['id']

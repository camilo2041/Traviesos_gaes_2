from django import forms
from .models import PQRS

class formulario_pqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['Tipo_pqrs','Descripcion']
        
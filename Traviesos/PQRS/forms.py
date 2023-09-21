from django import forms
from .models import PQRS

class FormAgendarPqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['Tipo_pqrs', 'Nombre', 'Descripcion']
        
    def __init__(self, *args, **kwargs):
        super(FormAgendarPqrs, self).__init__(*args, **kwargs)
        self.fields['Tipo_pqrs'].empty_label = "Seleccionar"
from django import forms
from .models import PQRS

class PQRSForm(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['Tipo_pqrs', 'Descripcion']

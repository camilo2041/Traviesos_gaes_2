from django import forms
from .models import PQRS, Tipo_pqrs

class FormAgendarPqrs(forms.ModelForm):
    Tipo_pqrs = forms.ModelChoiceField(
        queryset=Tipo_pqrs.objects.all(),
        empty_label="Seleccione un tipo",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = PQRS
        fields = ['Tipo_pqrs', 'Nombre', 'Descripcion']
        
        
    def __init__(self, *args, **kwargs):
        super(FormAgendarPqrs, self).__init__(*args, **kwargs)
        self.fields['Tipo_pqrs'].empty_label = "Seleccionar"
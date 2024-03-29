from django import forms
from .models import AgendarCita, Mascota, Tamaño, Raza

class FormAgendarCita(forms.ModelForm):
    class Meta:
        model = AgendarCita
        fields = '__all__'
        
    Nombre = forms.ModelChoiceField(
        queryset=Mascota.objects.all(),
        empty_label="Seleccionar una mascota",
        to_field_name='nombre',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    
class informacion_mascota(forms.ModelForm):
        class Meta:
            model = Mascota
            fields = ['nombre','raza','peso','Tamaño','edad']
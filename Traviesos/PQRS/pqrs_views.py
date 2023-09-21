from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tipo_pqrs
from .forms import FormAgendarPqrs

def formulario_pqrs(request):
    if request.method == 'POST':
        form = PQRSForm(request.POST)
        if form.is_valid():
            pqrs = form.save(commit=False)
            pqrs.usuario = request.user  # Asigna el usuario actual
            pqrs.save()
            return redirect('página_de_confirmación')  # Puedes redirigir a una página de confirmación o a donde desees.
    else:
        form = PQRSForm()
    
    return render(request, 'formulario_pqrs.html', {'form': form})
def mostrar_formulario(request):
    return render(request, 'PQRS/form.html')

@login_required
def pqrs (request):
    return render(request,'PQRS/form.html', {'user': request.user})

def coment (request):
    return render(request, 'PQRS/coment.html')


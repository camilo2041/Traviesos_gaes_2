from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PQRS
from .forms import formulario_pqrs

@login_required
def lista_pqrs(request):
    pqrs_del_usuario = PQRS.objects.filter(usuario=request.user)
    return render(request, 'PQRS/lista_pqrs.html', {'pqrs_del_usuario': pqrs_del_usuario})

def formulariopqrs(request):
    if request.method == 'POST':
        form = formulario_pqrs(request.POST)
        if form.is_valid():
            informacion = form.save(commit=False)
            informacion.usuario = request.user 
            informacion.save()
            messages.success(request, 'Cita guardada correctamente.')
            return redirect('pqrs')
    else:
        form = formulario_pqrs()
    return render(request, 'formulario_pqrs.html', {'form': form})

def mostrar_formulario(request):
    return render(request, 'PQRS/form.html')

@login_required
def pqrs (request):
    return render(request,'PQRS/form.html', {'user': request.user})

def coment (request):
    return render(request, 'PQRS/coment.html')


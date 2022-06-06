from django.shortcuts import render, redirect
from .models import FormDatos
from .forms import FormDatos

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def comprar(request):
    return render(request, 'core/comprar.html')

def gatos(request):
    return render(request, 'core/gatos.html')

def perros(request):
    return render(request, 'core/perros.html')

def login(request):
    return render(request, 'core/login.html')

def reestablecer(request):
    return render(request, 'core/reestablecer.html')

def perfil(request):
    datosCliente = FormDatos()
    datos = {
        'datosCliente': datosCliente
    }
    return render(request, 'core/perfil.html',datos)

def registro(request):
    datos = {
        'form':FormDatos()
    }
    if request.method == 'POST':
        formulario = FormDatos(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Registrado correctamente"
    return render(request, 'core/registro.html', datos)

def mod_perfil(request, id):
    formulario = FormDatos.objects.get(idRut=id)
    datos = {
        'form': FormDatos(instance=formulario)
    }
    if request.method == 'POST':
        formulario = FormDatos(data=request.POST, instance=formulario)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/mod_perfil.html', datos)

def eliminar_perfil(request, id):
    formulario = FormDatos.objects.get(idRut=id)
    formulario.delete()
    return redirect(to="perfil")

def sobrenosotros(request):
    return render(request, 'core/sobrenosotros.html')

def ubicanos(request):
    return render(request, 'core/ubicanos.html')


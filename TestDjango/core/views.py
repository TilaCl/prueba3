from django.shortcuts import render

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

def registro(request):
    return render(request, 'core/registro.html')

def sobrenosotros(request):
    return render(request, 'core/sobrenosotros.html')

def ubicanos(request):
    return render(request, 'core/ubicanos.html')


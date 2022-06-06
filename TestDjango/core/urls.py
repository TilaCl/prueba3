from django.urls import path
from .views import index, carrito, comprar, gatos, login, perros, reestablecer, registro, sobrenosotros, ubicanos, perfil, registro, mod_perfil, eliminar_perfil

urlpatterns = [
    path('', index,name="index"),
    path('carrito', carrito, name="carrito"),
    path('comprar', comprar, name="comprar"),
    path('gatos', gatos, name="gatos"),
    path('login', login, name="login"),
    path('', perfil, name = "perfil"),
    path('registro.html', registro, name = "registro"),
    path('mod_perfil/<id>', mod_perfil, name = "mod_perfil"),
    path('eliminar_perfil/<id>', eliminar_perfil, name = "eliminar_perfil"),
    path('perros', perros, name="perros"),
    path('reestablecer', reestablecer, name="reestablecer"),
    path('sobrenosotros', sobrenosotros, name="sobrenosotros"),
    path('ubicanos', ubicanos, name="ubicanos"),
]  

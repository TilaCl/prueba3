from django.urls import path
from .views import index, carrito, comprar, gatos, login, perros, reestablecer, registro, sobrenosotros, ubicanos

urlpatterns = [
    path('', index,name="index"),
    path('carrito', carrito, name="carrito"),
    path('comprar', comprar, name="comprar"),
    path('gatos', gatos, name="gatos"),
    path('login', login, name="login"),
    path('perros', perros, name="perros"),
    path('reestablecer', reestablecer, name="reestablecer"),
    path('registro', registro, name="registro"),
    path('sobrenosotros', sobrenosotros, name="sobrenosotros"),
    path('ubicanos', ubicanos, name="ubicanos"),
]  
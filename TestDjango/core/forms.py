from django import forms
from django.forms import ModelForm
from .models import FormDatos

class FormDatos(ModelForm):
    class Meta:
        model = FormDatos
        fields = ['idRut', 'nombre', 'correo', 'contraseña', 'telefono']

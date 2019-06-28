from django import forms
from main.models import Proveedor,Equipo

class ProveedorEquipoForm(forms.Form):
    proveedor = forms.CharField(min_length=2, max_length=255)
    equipo = forms.CharField(min_length=2, max_length=255)
from django import forms
from main.models import  Sucursal


class UserForm(forms.Form):
    codigo = forms.CharField(required=False)
    username = forms.CharField(min_length=4, max_length=150)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=150, min_length=6)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=150, min_length=6)
    # sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.exclude(cl_estado=False), required=False)
    correo = forms.EmailField()


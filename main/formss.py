
from django import forms
from main.models import Menu, Rol, User,Sucursal
from django.core.validators import RegexValidator
from django.forms import ModelForm,Textarea,CharField
from django.contrib.auth.forms import UserCreationForm



class frm_login(forms.Form):
    username = forms.CharField(max_length=100, label='Usuario')
    password = forms.CharField(label='Password',widget=forms.PasswordInput ,max_length=150)

class CrtRolForm(forms.Form):
    codigo      = forms.CharField(min_length=4,max_length=4,required=True)
    nombre      = forms.CharField(min_length=4,max_length=150,label="rol")
    desc        = forms.CharField(min_length=4,max_length=254,widget=forms.Textarea(attrs={'rows':3}))
    estado      = forms.BooleanField()

class CrearMenuForm(forms.Form):
    codigo      =forms.CharField(min_length=6,max_length=6,required=True)
    nombre      =forms.CharField(min_length=4,max_length=100,required=True)
    desc        =forms.CharField(min_length=4,max_length=255,widget=forms.Textarea(attrs={'rows':3}))
    menuS       =forms.ModelChoiceField(queryset=Menu.objects.filter(fk_menu_codigo=None), required=False)
    url         =forms.CharField(min_length=4,max_length=255, required=False)
    icono       =forms.CharField(min_length=4,max_length=20)
    estado      =forms.BooleanField(label='Activo',required=False)

class EditarMenuForm(forms.Form):
    codigo      =forms.CharField(min_length=6,max_length=6, required=False)
    nombre      =forms.CharField(min_length=4,max_length=100,required=True)
    desc        =forms.CharField(min_length=4,max_length=255,widget=forms.Textarea(attrs={'rows':3}))
    menuS       =forms.ModelChoiceField(queryset=Menu.objects.filter(fk_menu_codigo=None), required=False)
    url         =forms.CharField(min_length=4,max_length=255, required=False)
    icono       =forms.CharField(min_length=4,max_length=20)
    estado      =forms.BooleanField(label='Activo',required=False)


# ----------------------------------------------------------------------------------------------    |  R O L E S

class RolForm(forms.Form):
    codigo  =   forms.CharField(min_length=8, max_length=8)
    nombre  =   forms.CharField(min_length=3, max_length=100)
    desc    =   forms.CharField(min_length=3, max_length=255, widget=forms.Textarea(attrs={'rows': 3}))
    estado  =   forms.BooleanField(label='Activo', required=False)


    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        try:
            rol=Rol.objects.get(pk_codigo=codigo)
        except Rol.DoesNotExist:
            return codigo
        raise forms.ValidationError('El codigo del rol ya se encuentra registrado')

    def clean_nombre(self):
        nombre=self.cleaned_data['nombre']
        try:
            rol=Rol.objects.get(ct_nombre=nombre)
        except Rol.DoesNotExist:
            return nombre
        raise forms.ValidationError('El nombre del rol ya se encuentra registrado')

class EditRolForm(forms.Form):
    codigo = forms.CharField(min_length=8, max_length=8)
    nombre = forms.CharField(min_length=3, max_length=100)
    desc = forms.CharField(min_length=3, max_length=255, widget=forms.Textarea(attrs={'rows': 3}))
    estado = forms.BooleanField(label='Activo', required=False)

    def __init__(self, *args, **kwargs):
        super(EditRolForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['readonly'] = True



# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
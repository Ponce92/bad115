from django import forms
from main.models import Menu



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

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['codigo','menuS']
        else:
            return []

# ----------------------------------------------------------------------------------------------



class RolForm(forms.Form):
    codigo  =   forms.CharField(min_length=8,max_length=8,required=False)
    nombre  =   forms.CharField(min_length=3,max_length=100)
    desc    =   forms.CharField(min_length=3,max_length=255,widget=forms.Textarea(attrs={'rows':3}))
    estado  =   forms.BooleanField(label='Activo',required=False)
    def get_readonly_fields(self,request, obj=None):
        if obj:
            return ["codigo"]
        else:
            return []
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
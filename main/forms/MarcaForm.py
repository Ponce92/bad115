from django import forms
from main.models import Marca


class MarcaCreateForm(forms.Form):
    codigo = forms.CharField(min_length=8, max_length=8)
    nombre = forms.CharField(min_length=6, max_length=255)
    desc = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    estado=forms.BooleanField(required=False)
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            suc = Marca.objects.get(ct_nombre=nombre)
        except Marca.DoesNotExist:
            return nombre
        raise forms.ValidationError('El nombre de la sucursal ya se encuentra registrado')

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        try:
            marc = Marca.objects.get(pk_codigo=codigo)
        except Marca.DoesNotExist:
            return codigo
        raise forms.ValidationError('El telefono ya se encuentra registrado')

class MarcaEditForm(forms.Form):
    codigo = forms.CharField(min_length=8, max_length=8)
    nombre = forms.CharField(min_length=2, max_length=255)
    desc = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    estado=forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(MarcaEditForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['readonly'] = True

    def clean(self):
        frm = self.cleaned_data
        cod = frm['codigo']
        nombre=frm['nombre']
        if(Marca.objects.filter(ct_nombre=nombre).exclude(pk_codigo=cod).exists()):
            self._errors['nombre'] = ['El nombre ya se encuentra registrado']
from django import forms
from main.models import CategoriaEquipo

class CategoriaForm(forms.Form):
    codigo = forms.CharField(min_length=6, max_length=6)
    nombre = forms.CharField(min_length=6, max_length=255)
    desc = forms.CharField(min_length=4, max_length=255, widget=forms.Textarea(attrs={'rows': 3}))
    estado = forms.BooleanField(required=False)

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        try:
            obj = CategoriaEquipo.objects.get(pk_codigo=codigo)
        except CategoriaEquipo.DoesNotExist:
            return codigo
        raise forms.ValidationError('El codigo ingresado ya existe en la base de datos')

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            obj = CategoriaEquipo.objects.get(ct_nombre = nombre)
        except CategoriaEquipo.DoesNotExist:
            return nombre
        raise forms.ValidationError('El nombre de la categoria ya se encuentra registrado.')

class CategoriaEditForm(forms.Form):
    codigo = forms.CharField(min_length=6, max_length=6)
    nombre = forms.CharField(min_length=6, max_length=255)
    desc = forms.CharField(min_length=4, max_length=255, widget=forms.Textarea(attrs={'rows': 3}))
    estado = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(CategoriaEditForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['readonly'] = True

    def clean(self):
        form = self.cleaned_data
        if (CategoriaEquipo.objects.filter(ct_nombre=form['nombre']).exclude(pk_codigo=form['codigo']).exists()):
            self._errors['nombre'] = ['El nombre ya se encuentra registrado']

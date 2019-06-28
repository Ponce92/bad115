from django import forms

from main.models import Equipo,CategoriaEquipo

class EquipoForm(forms.Form):
    nombre = forms.CharField(min_length=6, max_length=255)
    desc = forms.CharField(min_length=4, max_length=255, widget=forms.Textarea(attrs={'rows': 3}))
    categoria= forms.ModelChoiceField(queryset=CategoriaEquipo.objects.filter(cl_estado=True))
    estado = forms.BooleanField(required=False)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            obj = Equipo.objects.get(ct_nombre = nombre)
        except Equipo.DoesNotExist:
            return nombre
        raise forms.ValidationError('El nombre del equipo ya se encuentra registrado.')

class EquipoEditForm(forms.Form):
    codigo = forms.CharField(required=False)
    categoria=forms.ModelChoiceField(queryset=CategoriaEquipo.objects.filter(cl_estado=True))
    nombre = forms.CharField(min_length=6, max_length=255)
    desc = forms.CharField(min_length=4, max_length=255, widget=forms.Textarea(attrs={'rows': 3}))
    estado = forms.BooleanField(required=False)


    def __init__(self, *args, **kwargs):
        super(EquipoEditForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['categoria'].widget.attrs['readonly'] = True

    def clean(self):
        form = self.cleaned_data
        if (Equipo.objects.filter(ct_nombre=form['nombre']).exclude(pk_codigo=form['codigo']).exists()):
            self._errors['nombre'] = ['El nombre ya se encuentra registrado']

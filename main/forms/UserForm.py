from django import forms
from main.models import Sucursal,Rol, User


class UserForm(forms.Form):
    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(cl_estado=True).exclude(ct_nombre='Admin IT'))
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.filter(cl_estado=True))
    estado = forms.BooleanField(required=False)
    email = forms.EmailField()
    codigo=forms.CharField(min_length=8, max_length=8)
    username = forms.CharField(min_length=4, max_length=25)
    password1 = forms.CharField(min_length=4, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=4, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
           obj = User.objects.get(username=username)
        except User.DoesNotExist:
           return username
        raise forms.ValidationError('El nombre nombre de usuario ya se encuentra registrado.')
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        try:
           obj = User.objects.get(pk_codigo=codigo)
        except User.DoesNotExist:
           return codigo
        raise forms.ValidationError('El nombre nombre de usuario ya se encuentra registrado.')
    def clean_email(self):
        correo = self.cleaned_data['email']
        try:
            obj = User.objects.get(email=correo)
        except User.DoesNotExist:
            return correo
        raise forms.ValidationError('El correo electronico especificado ya se encuentra registrado')



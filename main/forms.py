from django import forms


class frm_login(forms.Form):
    username = forms.CharField(max_length=100, label='Usuario')
    password = forms.CharField(label='Password',widget=forms.PasswordInput ,max_length=150)

class CrtRolForm(forms.Form):
    codigo      = forms.CharField(min_length=4,max_length=4,required=True)
    nombre      = forms.CharField(min_length=4,max_length=150,label="Rol ...")
    desc        = forms.CharField(min_length=4,max_length=254,widget=forms.Textarea(attrs={'rows':3}))
    estado      = forms.BooleanField(required=True)


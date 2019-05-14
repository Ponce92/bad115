from django import forms


class frm_login(forms.Form):
    user_name = forms.CharField(max_length=100, label='Usuario')
    user_pass = forms.CharField(label='Password',widget=forms.PasswordInput ,max_length=150)
     
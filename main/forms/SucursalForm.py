from django import forms
from django.core.validators import RegexValidator
from main.models import Menu, Rol, User,Sucursal,Permiso
telefonoValidator=RegexValidator(r'\d{4}\-\d{4}', 'El formato no es adecuado, ejem: ####-#### ')
from django.db      import connection

class SucursalForm(forms.Form):
    # codigo=forms.CharField(min_length=8,max_length=8,)
    nombre=forms.CharField(min_length=6, max_length=255)
    dir=forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    correo=forms.EmailField()
    telefono=forms.CharField(min_length=9,max_length=9, validators=[telefonoValidator])
    estado=forms.BooleanField(required=False)
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            suc = Sucursal.objects.get(ct_nombre=nombre)
        except Sucursal.DoesNotExist:
            return nombre
        raise forms.ValidationError('El nombre de la sucursal ya se encuentra registrado')
    def clean_correo(self):
        correo = self.cleaned_data['correo']
        try:
            suc = Sucursal.objects.get(ct_correo=correo)
        except Sucursal.DoesNotExist:
            return correo
        raise forms.ValidationError('El correo electronico ya se encuentra registrado')
    def clean_telefono(self):
        tel = self.cleaned_data['telefono']
        try:
            suc = Sucursal.objects.get(ct_telefono=tel)
        except Sucursal.DoesNotExist:
            return tel
        raise forms.ValidationError('El telefono ya se encuentra registrado')

class SucursalEditForm(forms.Form):
    codigo=forms.CharField(required=False)
    nombre=forms.CharField(min_length=6, max_length=255)
    dir=forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    correo=forms.EmailField()
    telefono=forms.CharField(min_length=9,max_length=9, validators=[telefonoValidator])
    estado=forms.BooleanField(required=False)
    edit = forms.BooleanField(required=False,widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(SucursalEditForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['readonly'] = True

    def clean(self):
        form=self.cleaned_data
        if form['edit'] ==True:
            var = form['codigo']
            if(Sucursal.objects.filter(ct_nombre=form['nombre']).exclude(pk_codigo=form['codigo']).exists()):
                self._errors['nombre']=['El nombre ya se encuentra registrado']
            if (Sucursal.objects.filter(ct_correo=form['correo']).exclude(pk_codigo=form['codigo']).exists()):
                self._errors['correo'] = ['El correo ya se encuentra registrado']
            if (Sucursal.objects.filter(ct_telefono=form['telefono']).exclude(pk_codigo=form['codigo']).exists()):
                self._errors['telefono'] = ['El Telefono ya se encuentra registrado']
#
#
#
def getMenus(rol):
    '''Retorna los menus asociados a un rol en especifico'''
    cursor = connection.cursor()
    cursor.callproc('bsp_get_menus_roles', [True, rol.pk_codigo])
    menus = list()
    for row in cursor.fetchall():
        menu = Menu()
        menu.pk_codigo = row[0]
        try:
            menu.fk_menu_codigo = Menu.objects.get(pk_codigo=row[1])
        except:
            menu.fk_menu_codigo = None

        menu.ct_nombre = row[2]
        menu.cd_descripcion = row[3]
        menu.ct_url = row[5]

        menus.append(menu)

    return menus

def getUser(codigo):
    user = User.objects.get(username=codigo)
    return user

def func_get_permisos(rol):
    cursor = connection.cursor()
    cursor.callproc('bsp_get_permisos_roles', [True, rol.pk_codigo])
    permisos = list()
    for row in cursor.fetchall():
        per = Permiso()
        per.pk_codigo = row[0]
        per.ct_nombre = row[1]
        per.cd_descripcion = row[2]

        permisos.append(per)

    return permisos
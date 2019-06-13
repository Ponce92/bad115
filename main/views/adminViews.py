from django.shortcuts                   import render
from django.shortcuts                   import redirect
from django.http                        import JsonResponse
from django.template.loader             import render_to_string
from django.contrib.auth.decorators     import login_required
from django.contrib                     import messages
from django.views.generic.list          import ListView
from django.core.paginator              import Paginator

from django.db      import connection
from main.forms import CrtRolForm, EditarMenuForm
from  main.forms    import CrearMenuForm,RolForm,UserForm
from main.models    import *

#-----------------------------------------------------------------------------------------------------| Roles
@login_required
def get_roles(request):
    roles_list = Rol.objects.all()
    paginator = Paginator(roles_list, 8)

    page = request.GET.get('page')
    roles = paginator.get_page(page)

    context={
        'roles':roles,
        'User': getUser(request.user),
        'Menus': getMenus(getUser(request.user).fk_rol_codigo)
    }
    return render(request,'admin/roles/roles.html',context)

@login_required
def create_rol(request):
    if request.method == 'POST':
        form =RolForm(request.POST)
        if form.is_valid():
            #Salvamos el valor de la
            rol= Rol()
            rol.pk_codigo = form.cleaned_data['codigo']
            rol.ct_nombre = form.cleaned_data['nombre']
            rol.cd_descripcion  = form.cleaned_data['desc']
            rol.cl_estado = form.cleaned_data['estado']
            rol.cl_editable=False
            rol.save()
            messages.add_message(request, messages.SUCCESS, 'Rol almacenado correctamente')
            # try:
            #
            # except:
            #     messages.add_message(request,messages.ERROR,'Ha ocurrido un error al insertar el nuevo rol')
            return redirect('roles')
    elif request.method =='GET':
        form=RolForm(initial={'estado': False})
        context={
            'form':form
            }
        html=render_to_string('admin/roles/crear.html', context, request=request)
        return JsonResponse({'html_form':html})

def validar_rol(request):
    if request.method == 'POST':
        form=RolForm(request.POST)
        if form.is_valid():
            res=True
        else:
            res=False
        context = {
            'form': form
        }
        html = render_to_string('admin/roles/crear.html', context, request=request)
        return JsonResponse({'html_form': html, 'res': res})
    else:
        return redirect('roles')

@login_required
def delete_rol(request,id):
    pass

def editar_rol(request,codigo):
    if request.method == 'POST':
        pass
    elif request.method =='GET':
        rol = Rol.objects.get(pk_codigo=codigo)
        form=RolForm(initial={
            'codigo':rol.pk_codigo,
            'nombre':rol.ct_nombre,
            'desc':rol.cd_descripcion,
            'estado':rol.cl_estado
        })
        context = {
            'form': form
        }
        html = render_to_string('admin/roles/editar.html', context, request=request)
        return JsonResponse({'html_form': html})

def permisos_roles(request,codigo):
    rol=Rol.objects.get(pk_codigo=codigo)
    cursor=connection.cursor()

    cursor.callproc('bsp_get_permisos_roles', [True, codigo])

    permisos = list()
    for row in cursor.fetchall():
        per = Permiso()
        per.pk_codigo = row[0]
        per.ct_nombre = row[1]
        per.cd_descripcion = row[2]

        permisos.append(per)
    context={
        'rol': rol,
        'permisos': permisos,
        'Menus':getMenus(getUser(request.user).fk_rol_codigo)
    }
    return render(request, 'admin/roles/permisos.html', context)

def get_permisos(request,codigo):
    cursor = connection.cursor()
    cursor.callproc('bsp_get_permisos_roles', [False, codigo])

    permisos=list()
    for row in cursor.fetchall():
        per=Permiso()
        per.pk_codigo=row[0]
        per.ct_nombre=row[1]
        per.cd_descripcion=row[2]

        permisos.append(per)

    context = {
        'permisos': permisos
    }
    html = render_to_string('admin/roles/permisosOpciones.html', context, request=request)
    return JsonResponse({'html_form': html})

def agregar_permiso(request):
    idRol=request.POST['rol']
    idPermiso=request.POST['permiso']

    try:
        perm = Permiso.objects.get(pk_codigo=idPermiso)
        rol = Rol.objects.get(pk_codigo=idRol)
        pr = PermisoRol()
        pr.fk_permiso_codigo = perm
        pr.fk_rol_codigo = rol

        pr.save()
        messages.add_message(request, messages.SUCCESS, "se ha agregado el rol correctamente")
    except:
        messages.add_message(request, messages.ERROR, "El servidor a fracasado al realizar la operacion")
    return redirect('permisos_roles',codigo=idRol)

def eliminar_permiso(request):
    idR=request.POST['role']
    idP=request.POST['permisoe']

    try:
        pr=PermisoRol.objects.get(fk_rol_codigo=idR,fk_permiso_codigo=idP)
        pr.delete()
        messages.add_message(request, messages.SUCCESS, "Se ha eliminado satisfactoriamente el permiso del rol")
    except:
        messages.add_message(request, messages.ERROR, "El servidor a fracasado al realizar la operacion")
    return redirect('permisos_roles',codigo=idR)

def roles_menus(request,codigo):
    rol = Rol.objects.get(pk_codigo=codigo)
    cursor = connection.cursor()
    cursor.callproc('bsp_get_menus_roles', [True, codigo])
    menus=list()
    for row in cursor.fetchall():
        menu = Menu()
        menu.pk_codigo = row[0]
        try:
            menu.fk_menu_codigo = Menu.objects.get(pk_codigo=row[1])
        except:
            menu.fk_menu_codigo=None

        menu.ct_nombre = row[2]
        menu.cd_descripcion=row[3]
        menu.ct_url=row[5]

        menus.append(menu)
    context = {
        'rol': rol,
        'menus':menus,
        'User': getUser(request.user),
        'Menus': getMenus(getUser(request.user).fk_rol_codigo)
    }

    return render(request,'admin/roles/menus.html', context)

def get_menus(request,codigo):
    cursor = connection.cursor()
    cursor.callproc('bsp_get_menus_roles', [False, codigo])

    menus = list()
    for row in cursor.fetchall():
        menu = Menu()
        menu.pk_codigo = row[0]
        menu.ct_nombre = row[2]
        menu.cd_descripcion = row[3]
        menu.ct_url = row[5]
        try:
            menu.fk_menu_codigo = Menu.objects.get(pk_codigo=row[1]);
        except:
            menu.fk_menu_codigo =None
        menus.append(menu)
    context = {
        'menus': menus
    }
    html = render_to_string('admin/roles/menusOpciones.html', context, request=request)
    return JsonResponse({'html_form': html})

def agregar_menu_rol(request):
    idRol=request.POST['rol']
    idMenu=request.POST['menu']

    rol=Rol.objects.get(pk_codigo=idRol)
    menu=Menu.objects.get(pk_codigo=idMenu)

    menuRol=RolMenu()
    menuRol.fk_menu_codigo=menu
    menuRol.fk_rol_codigo=rol

    try:
        menuRol.save()
        messages.add_message(request,messages.SUCCESS,"El menu se ha agregado al rol correctamente")
    except:
        messages.add_message(request,messages.ERROR,"Ha ocurrido un problema al processar la solicitud")

    return redirect('roles_menus',codigo=idRol)

def eliminar_menu_rol(request):
    idR = request.POST['role']
    idM = request.POST['menue']

    try:
        pr = RolMenu.objects.get(fk_rol_codigo=idR, fk_menu_codigo=idM)
        pr.delete()
        messages.add_message(request, messages.SUCCESS, "Se ha eliminado satisfactoriamente el permiso del rol")
    except:
        messages.add_message(request, messages.ERROR, "El servidor a fracasado al realizar la operacion")
    return redirect('roles_menus',codigo=idR)
#--------------------------------------------------------------------------------------------------|    Menus
@login_required
def get_menu(request):
    user=request.user
    menuList=Menu.objects.all()
    crearFrm=CrearMenuForm()
    return render(request,'admin/menus/menus.xhtml',{'user':user,'menuList':menuList,'crearForm':crearFrm})

def validar_menu(request):
    res=False
    if request.method == 'POST':
        form =CrearMenuForm(request.POST)
        if form.is_valid():
            res=True
    else:
        form=CrearMenuForm(initial={'estado':False})

    context={
        'crearForm' : form
        }
    html=render_to_string('admin/roles/crear.html',context,request=request)
    return JsonResponse({'html_form': html,'res': res})

def crear_menu(request):
    if request.method =='POST':
        form = CrearMenuForm(request.POST)
        if form.is_valid():
            menu = Menu()
            menu.pk_codigo = form.cleaned_data['codigo']
            menu.fk_menu_codigo = form.cleaned_data['menuS']
            menu.ct_nombre = form.cleaned_data['nombre']
            menu.cd_descripcion = form.cleaned_data['desc']
            menu.ct_icono = form.cleaned_data['icono']
            menu.ct_url = form.cleaned_data['url']
            bl = form.cleaned_data['estado']
            if bl:
                menu.cl_estado = 'ACT'
            else:
                menu.cl_estado = 'INA'

            try:
                menu.save()
                res = True
                messages.add_message(request,messages.INFO, 'El menu ha sido almacenado correctamente')
                redirect('menus')
            except:
                messages.add_message(request,messages.ERROR, 'No se ha logrado completar la trasaccion')
                res = False
    return redirect('menus')

def eliminar_menu(request, codigo):
    cursor=connection.cursor()
    cursor.callproc('bsp_delete_menu', [codigo, None,None])
    res=cursor.fetchall()[0]
    cursor.close()
    if res[0] == 'WARN':
        messages.add_message(request, messages.WARNING, res[1])
    if res[0] == 'SUCCESS':
        messages.add_message(request, messages.SUCCESS, res[1])
    if res[0] == 'ERROR':
        messages.add_message(request, messages.ERROR, res[1])
            
    return redirect('menus')

def editar_menu(request):
    if request.method == 'POST':
        form = CrearMenuForm(request.POST)
        if form.is_valid():
            menu = Menu.objects.get(pk_codigo=form.cleaned_data['codigo'])
            menu.fk_menu_codigo = form.cleaned_data['menuS']
            menu.ct_nombre = form.cleaned_data['nombre']
            menu.cd_descripcion = form.cleaned_data['desc']
            menu.ct_icono = form.cleaned_data['icono']
            menu.ct_url = form.cleaned_data['url']
            bl = form.cleaned_data['estado']
            if bl:
                menu.cl_estado = 'ACT'
            else:
                menu.cl_estado = 'INA'
            try:
                menu.save()
                messages.add_message(request,messages.INFO, 'EL registro se actualizado correctamente')
            except:
                messages.add_message(request, messages.WARNING, 'Error en la acutalizacion del registro')
    return redirect('menus')

def menu_actualizar_ajax(request, codigo):
    menu = Menu.objects.get(pk_codigo=codigo)
    form = EditarMenuForm({'codigo': menu.pk_codigo,
                          'nombre':menu.ct_nombre,
                          'desc':menu.cd_descripcion,
                          'menuS':menu.fk_menu_codigo,
                          'url':menu.ct_url,
                          'icono':menu.ct_icono,
                           'estado':menu.cl_estado
                          })
    context = {
        'editarForm': form
    }
    html = render_to_string('admin/menus/editar.html', context, request=request)
    return JsonResponse({'html_form': html})
# ----------------------------------------------------------------------------------------
#       Metodos de Permisos
# ----------------------------------------------------------------------------------------

def crear_permiso(request):
    if request.method=='POST':
        pass
    elif request.method=='GET':
        form = None
        context = {
            'form': form
        }
        html = render_to_string('admin/permisos/crear.html', context, request=request)
        return JsonResponse({'html_form': html})

def get_usuarios(request):
    user=getUser(request.user)

    context={
        'User': user,
        'Menus': getMenus(user.fk_rol_codigo)
    }
    return render(request,'admin/usuarios/usuarios.html',context)

def crear_usuario(request):
    '''Metodo ajax que retorna el formulario de registro de los usuarios o ejecuta la accion de guardar '''
    if request.method == 'GET':
        form = UserForm(initial={'cl_estado':False})
        context = {
            'form': form
        }
        html = render_to_string('admin/usuarios/crear.html', context, request=request)
        return JsonResponse({'html_form': html})
    elif request.method == 'POST':
        pass


def validar_usuario():
    '''Metodo ajax que valida el formulario de registro de un usuario retorna true o false '''
    pass

# ----------------------------------------------------------------------------------------
#       List views
# ----------------------------------------------------------------------------------------

class RolesList(ListView):
    model = Rol
    paginate_by = 9
    template_name = 'admin/roles/roles.html'

class PermisosList(ListView):
    model = Permiso
    paginate_by = 9
    template_name = 'admin/permisos/permisos.html'


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


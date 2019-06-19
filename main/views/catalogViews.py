from django.shortcuts                   import render
from django.shortcuts                   import redirect
from django.http                        import JsonResponse
from django.template.loader             import render_to_string
from django.contrib                     import messages
from django.http                        import Http404
from django.shortcuts import get_object_or_404
from django.db      import connection
from django.contrib.auth.decorators     import login_required


from main.models import CategoriaEquipo
from main.models    import Sucursal,User,Menu,Permiso
from main.forms import SucursalForm,SucursalEditForm,CategoriaForm,CategoriaEditForm





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def equipo_eliminar(request):
    pass
def equipo_editar(request):
    pass

def equipo_validar(request):
    pass

def equipo_crear(request):
    pass

@login_required(login_url='/sgiee/security/login/')
def equipos(request):
    user = getUser(request.user)
    permisos = func_get_permisos(user.fk_rol_codigo)
    count = 0
    for res in permisos:
        if (res.ct_nombre == "puede_leer_equipo"):
            count = 100
    if count == 0:
        raise Http404("El recurso no se encuentra disponible")
    #---------------------------------------------------------
    equipos = None
    context = {
        'equipos': equipos,
        'Permisos': permisos,
        'User': getUser(request.user),
        'Menus': getMenus(getUser(request.user).fk_rol_codigo)
    }
    return render(request, 'catalog/equipos/equipos.html', context)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def categoria_eliminar(request):
    pass

def categoria_editar(request,codigo):
    print(codigo +'---------------------------------------------')
    if request.method =='POST':
        form = CategoriaEditForm(request.POST)
        if form.is_valid():
            obj=get_object_or_404(CategoriaEquipo, pk=form.cleaned_data['codigo'])

            obj.ct_nombre=form.cleaned_data['nombre']
            obj.cd_descripcion= form.cleaned_data['desc']
            obj.cl_estado  = form.cleaned_data['estado']

            obj.save()

            messages.add_message(request,messages.SUCCESS,'La categoria se ha acutualizado correctamente.')
        return redirect('categoria')
    elif request.method == 'GET':
        obj = get_object_or_404(CategoriaEquipo,pk=codigo)
        form= CategoriaEditForm(initial={
            'codigo':obj.pk_codigo,
            'nombre':obj.ct_nombre,
            'desc':obj.cd_descripcion,
            'estado':obj.cl_estado,
        })
        context = {
            'form': form
        }
        html = render_to_string('catalog/categorias/editar.html', context, request=request)
        return JsonResponse({'html_form': html})

def categoria_validar(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            res = True
        else:
            res = False
        context = {
            'form': form
        }
        html = render_to_string('catalog/categorias/crear.html', context, request=request)
        return JsonResponse({'html_form': html, 'res': res})
    elif request.method == 'GET':
        form = CategoriaEditForm(request.GET)
        if form.is_valid():
            res = True
        else:
            res = False
        context = {
            'form': form
        }
        html = render_to_string('catalog/categorias/editar.html', context, request=request)
        return JsonResponse({'html_form': html, 'res': res})

def categoria_crear(request):
    if request.method =='POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            try:
                cat = CategoriaEquipo()

                cat.pk_codigo = form.cleaned_data['codigo']
                cat.ct_nombre = form.cleaned_data['nombre']
                cat.cd_descripcion = form.cleaned_data['desc']
                cat.cl_estado=form.cleaned_data['estado']

                cat.save()
                messages.add_message(request,messages.SUCCESS,"La categoria se ha almacenado con exito")
            except:
                messages.add_message(request, messages.SUCCESS, "Error inesperado en la insersion de la categoria.")
        return redirect('categoria')
    elif request.method == 'GET':
        form = CategoriaForm()
        context = {
            'form': form
        }
        html = render_to_string('catalog/categorias/crear.html', context, request=request)
        return JsonResponse({'html_form': html})

@login_required(login_url='/sgiee/security/login/')
def categoria(request):
    user = getUser(request.user)
    permisos = func_get_permisos(user.fk_rol_codigo)
    count = 0
    for res in permisos:
        if (res.ct_nombre == "puede_leer_categoria_equipo"):
            count = 100
    if count == 0:
        raise Http404("El recurso no se encuentra disponible")
    #---------------------------------------------------------
    list =CategoriaEquipo.objects.all()
    context = {
        'list': list,
        'Permisos': permisos,
        'User': getUser(request.user),
        'Menus': getMenus(getUser(request.user).fk_rol_codigo)
    }
    return render(request, 'catalog/categorias/categorias.html', context)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def editar_sucursal(request,codigo):
    if request.method =='POST':
        form = SucursalEditForm(request.POST)
        if form.is_valid():
            suc=get_object_or_404(Sucursal,pk=form.cleaned_data['codigo'])

            suc.ct_nombre=form.cleaned_data['nombre']
            suc.cd_direccion= form.cleaned_data['dir']
            suc.ct_correo  = form.cleaned_data['correo']
            suc.ct_telefono= form.cleaned_data['telefono']
            suc.cl_estado  = form.cleaned_data['estado']

            suc.save()
            messages.add_message(request,messages.SUCCESS,'La sucursal ha sido actualizada correctamente')
        return redirect('sucursales')
    elif request.method == 'GET':
        suc = get_object_or_404(Sucursal, pk=codigo)
        form= SucursalEditForm(initial={
            'codigo':suc.pk_codigo,
            'nombre':suc.ct_nombre,
            'dir':suc.cd_direccion,
            'telefono':suc.ct_telefono,
            'correo':suc.ct_correo,
            'estado':suc.cl_estado,
            'edit': True
        })
        context = {
            'form': form
        }
        html = render_to_string('catalog/sucursal/editar.html', context, request=request)
        return JsonResponse({'html_form': html})

def validar_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            print("calidacion corretar")
            res = True
        else:
            res = False

        context = {
            'form': form
        }
        html = render_to_string('catalog/sucursal/crear.html', context, request=request)
        return JsonResponse({'html_form': html, 'res': res})
    elif request.method == 'GET':
        form = SucursalEditForm(request.GET)
        if form.is_valid():
            res = True
        else:
            res = False

        context = {
            'form': form
        }
        html = render_to_string('catalog/sucursal/editar.html', context, request=request)
        return JsonResponse({'html_form': html, 'res': res})

def crear_sucursal(request):
    if request.method =='POST':
        form=SucursalForm(request.POST)
        if form.is_valid():
        #      try:
            nombre= form.cleaned_data['nombre']
            telefono= form.cleaned_data['telefono']
            direccion= form.cleaned_data['dir']
            correo= form.cleaned_data['correo']
            estado= form.cleaned_data['estado']

            cursor = connection.cursor()
            cursor.callproc('bsp_insert_sucursal', [nombre,telefono, direccion, correo, estado])


            messages.add_message(request, messages.SUCCESS,"La sucursal se ha agregado correctamente")
             # except:
             #    messages.add_message(request, messages.SUCCESS, "El servidor no ha podido completar la transaccion")

        return redirect('sucursales')
    elif request.method == 'GET':
        form = SucursalForm(initial={'estado': False})
        context = {
            'form': form
        }
        html = render_to_string('catalog/sucursal/crear.html', context, request=request)
        return JsonResponse({'html_form': html})

@login_required(login_url='/sgiee/security/login/')
def sucursales(request):
    user = getUser(request.user)
    permisos = func_get_permisos(user.fk_rol_codigo)
    count = 0
    for res in permisos:
        if (res.ct_nombre == "puede_leer_sucursales"):
            count = 100
    if count == 0:
        raise Http404("El recurso no se encuentra disponible")
    # Se finaliza la validacion de los permisos requeridos---------------------------------

    # Logica de la funcion
    sucursales = Sucursal.objects.all()
    context = {
        'sucursales': sucursales,
        'Permisos': permisos,
        'User': getUser(request.user),
        'Menus': getMenus(getUser(request.user).fk_rol_codigo)
    }
    return render(request, 'catalog/sucursal/sucursales.html', context)

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

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
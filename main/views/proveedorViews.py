from django.shortcuts                   import render
from django.shortcuts                   import redirect
from django.http                        import JsonResponse
from django.template.loader             import render_to_string
from django.contrib                     import messages
from django.http                        import Http404
from django.shortcuts import get_object_or_404
from django.db import connection
from main.models import Permiso,Proveedor,User,Menu
from main.models import ProveedorEquipos,Equipo,CategoriaEquipo,Servicio,ProveedorServicios

from django.contrib.auth.decorators import login_required


def proveedor(request):
    pass

@login_required(login_url='/sgiee/security/login/')
def servicios(request):
    user = getUser(request.user)
    permisos = func_get_permisos(user.fk_rol_codigo)
    # count = 0
    # for res in permisos:
    #     if (res.ct_nombre == "puede_leer_marcas"):
    #         count = 100
    # if count == 0:
    #     raise Http404("El recurso no se encuentra disponible")

    prov = get_object_or_404(Proveedor, pk=user.pk_codigo)
    lista = ProveedorServicios.objects.filter(fk_proveedor_codigo=prov)
    list2 = Equipo.objects.filter(cl_estado=True)

    servicios = Servicio.objects.all()

    context = {
        'list': lista,
        'list2': list2,
        'list3': servicios,
        'proveedor': prov,
        'Permisos': permisos,
        'User': user,
        'Menus': getMenus(getUser(request.user).fk_rol_codigo)
    }
    return render(request, 'proveedor/servicios/servicios.html', context)

@login_required(login_url='/sgiee/security/login/')
def equipos(request):
    user = getUser(request.user)
    permisos = func_get_permisos(user.fk_rol_codigo)
    # count = 0
    # for res in permisos:
    #     if (res.ct_nombre == "puede_leer_marcas"):
    #         count = 100
    # if count == 0:
    #     raise Http404("El recurso no se encuentra disponible")

    prov = get_object_or_404(Proveedor, pk=user.pk_codigo)
    list = getEquipo(user.pk_codigo, True)
    list2 = getEquipo(user.pk_codigo, False)
    context = {
        'list': list,
        'list2' : list2,
        'proveedor' : prov,
        'Permisos': permisos,
        'User': user,
        'Menus': getMenus(getUser(request.user).fk_rol_codigo)
    }
    return render(request, 'proveedor/equipos/equipos.html', context)

def equipos_agregar(request):
    prov=request.POST.get('proveedor')
    eq= request.POST.get('equipo')
    pv=ProveedorEquipos()

    pv.fk_proveedor_codigo=get_object_or_404(Proveedor,pk=prov)
    pv.fk_equipo_codigo=get_object_or_404(Equipo,pk=eq)

    pv.save()
    messages.add_message(request,messages.SUCCESS,'El equipo se agrego con exito en sus productos ofertados')
    return redirect('proveedor_equipo')

def equipos_eliminar(request):
    eq = request.POST.get('codigo_el')
    equ= get_object_or_404(Equipo,pk=eq)
    eq = ProveedorEquipos.objects.filter(fk_equipo_codigo=equ)
    eq.delete()
    messages.add_message(request, messages.SUCCESS, 'Se completado con exito el processo, ya no es proveedor del equipo')
    return redirect('proveedor_equipo')




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

def getEquipo(codigo,bol):
    '''
    :param codigo: El codigo del proveedor
    :param bol: Bolean que indica el tipo de equipo a cargar
    :return: list de equipos ligados o no ligados al proveedor
    '''
    cursor = connection.cursor()

    cursor.callproc('bsp_get_equipo_ofertado', [codigo, bol])
    lista = list()

    for row in cursor.fetchall():
        eq = Equipo()
        eq.pk_codigo = row[0]
        try:
            eq.fk_categoria_codigo =CategoriaEquipo .objects.get(pk_codigo=row[1])
        except:
            eq.fk_categoria_codigo = None
        eq.ct_nombre = row[2]
        eq.cd_descripcion = row[3]
        lista.append(eq)

    cursor.close()
    return lista

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
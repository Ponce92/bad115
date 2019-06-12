from django.contrib.auth                import login,authenticate
from django.shortcuts                   import render
from django.shortcuts                   import redirect
from django.contrib.auth.decorators     import login_required
from main.models                        import User,Rol,Menu,RolMenu
from django.db      import connection



#--------------------------------------------------------------------------------------------------


@login_required()
def home(request):
    user = User.objects.get(username=request.user)
    menus= getMenus(user.fk_rol_codigo.pk_codigo)

    context={
        'User':user,
        'Menus':menus
    }
    print(menus)
    return render(request,'user/home.html',context)



def getMenus(codigo):
    '''Retorna los menus asociados a un rol en especifico'''
    cursor = connection.cursor()
    cursor.callproc('bsp_get_menus_roles', [True, codigo])
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
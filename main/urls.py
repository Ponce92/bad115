"""bad115 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.urls import path
from main.views import catalogViews    as cat
from main.views import adminViews       as admin
from main.views import defaultViews     as home

urlpatterns = [
    # path('login/',views.login,name='logi'),
    path('security/',include('django.contrib.auth.urls')),
    path('home/',home.home,name='home'),
    path('',home.home,name='home'),

#------------------------------------------------------------------------------------------------| Equipo electrico
    path('catalogos/equipos/',cat.equipos,name='equipos'),
    path('catalogos/equipos/crear/', cat.equipo_crear, name='crear_equipo'),
    path('catalogos/equipos/validar/', cat.equipo_validar, name='equipo_validar'),
    path('catalogos/equipos/editar/<str:codigo>/', cat.equipo_editar, name='equipo_editar'),
    path('catalogos/equipos/eliminar/<str:codigo>/', cat.equipo_eliminar, name='equipo_eliminar'),
#-----------------------------------------------------------------------------------------------------
    path('catalogos/categorias/', cat.categoria ,name='categoria'),
    path('catalogos/categorias/crear/', cat.categoria_crear, name='crear_categoria'),
    path('catalogos/categorias/validar/', cat.categoria_validar, name='validar_categoria'),
    path('catalogos/categorias/editar/<str:codigo>/', cat.categoria_editar, name='editar_categoria'),
    path('catalogos/categorias/eliminar/<str:codigo>/', cat.categoria_eliminar, name='eliminar_categoia'),

# -------------------------------------------------------------------------------------| Sucursales
    path('catalogos/sucursales/',cat.sucursales,name='sucursales'),
    path('catalogos/sucursales/crear/', cat.crear_sucursal, name='crear_sucursal'),
    path('catalogos/sucursales/validar/', cat.validar_sucursal, name='validar_sucursal'),
    path('catalogos/sucursales/editar/<str:codigo>/', cat.editar_sucursal, name='editar_sucursal'),



# Url hacia administracion de roles del sistema . . . . ...............................| Roles
    path('admin/roles/',admin.get_roles, name='roles'),
    path('admin/roles/crear/',admin.create_rol, name='crear_rol'),
    path('admin/roles/validar/',admin.validar_rol,name='validar_rol'),
    path('admin/roles/actualizar/<str:codigo>/',admin.editar_rol, name='editar_rol'),

    path('admin/roles/<str:codigo>/permisos/',admin.permisos_roles , name='permisos_roles'),
    path('admin/roles/permisos/agregar/',admin.agregar_permiso , name='agregar_permiso'),
    path('admin/roles/permisos/eliminar/',admin.eliminar_permiso , name='eliminar_permiso'),
    path('admin/roles/get/permisos/<str:codigo>/', admin.get_permisos, name='get_permisos'),

    path('admin/roles/<str:codigo>/menus/',admin.roles_menus, name='roles_menus'),
    path('admin/roles/<str:codigo>/get/menus/', admin.get_menus, name='get_menus'),
    path('admin/roles/menus/agregar/',admin.agregar_menu_rol,name='agregar_menu_rol'),
    path('admin/roles/menus/eliminar/', admin.eliminar_menu_rol, name='eliminar_menu_rol'),



    #Urls Crud de permisos ----------------------------------------------------|  Menus
    path('admin/permisos/',admin.PermisosList.as_view(),name='permisos' ),
    path('admin/permisos/crear',admin.crear_permiso,name='crear_permiso'),

    #Urls hacia amdinistracion de menus----------------------------------------------------|  Menus

    path('admin/menus/',admin.get_menu,name='menus'),
    path('admin/menus/crear',admin.crear_menu,name='crear_menu'),
    path('admin/menus/crear/validar',admin.validar_menu,name="validar_menu"),
    path('admin/menus/eliminar/<str:codigo>/',admin.eliminar_menu,name='menu_eliminar'),
    path('admin/menus/actualizar/', admin.editar_menu, name='menu_editar'),
    path('admin/menus/actualizar/ajax/<str:codigo>/', admin.menu_actualizar_ajax, name='menu_editar_get'),

    #UR  --------------------------------------------------------------------------------------------|    Usuarios
    path('admin/usuarios/',admin.get_usuarios,name='usuarios'),
    path('admin/usuarios/crear/',admin.crear_usuario,name='crear_user'),
    path('admin/usuarios/crear/validar/', admin.validar_usuario, name='validar_user')


]

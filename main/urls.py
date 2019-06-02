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
from main.views import adminViews       as admin
from main.views import defaultViews     as home

urlpatterns = [
    # path('login/',views.login,name='logi'),
    path('security/',include('django.contrib.auth.urls')),
    path('home/',home.home,name='home'),
    path('',home.home,name='home'),
    # Url hacia administracion de roles del sistema . . . . .
    path('roles/',admin.roles,name='roles'),
    path('roles/crear',admin.create_rol,name='rolCrear')

]

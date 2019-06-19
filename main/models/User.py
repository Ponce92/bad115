from django.db import models
from django.contrib.auth.models import AbstractUser

from .Rol import Rol
from .Sucursal import Sucursal

class User(AbstractUser):
    pk_codigo       = models.CharField(primary_key=True, max_length=8)
    fk_rol_codigo   = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_rol_codigo', blank=True, null=False)
    fk_sucursal_codigo = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='fk_sucursal_codigo', blank=True, null=True)
    username        = models.CharField(unique=True, max_length=150)
    email           = models.CharField(unique=True, max_length=255)
    password        = models.CharField(max_length=255)
    cn_intentos   = models.IntegerField(default=0)
    cl_estado      = models.BooleanField()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        managed = True
        db_table = 'bt_usuarios'
        app_label='main'

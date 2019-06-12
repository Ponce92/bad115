from django.db import models
from django.contrib.auth.models import AbstractUser

from .Rol import Rol

class User(AbstractUser):
    pk_codigo       = models.CharField(primary_key=True, max_length=8)
    fk_rol_codigo   = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_rol_codigo', blank=True, null=False)
    username        = models.CharField(unique=True, max_length=150)
    email           = models.CharField(unique=True, max_length=255)
    password        = models.CharField(max_length=255)
    user_attempts   = models.IntegerField(default=0)
    user_state      = models.CharField(max_length=3)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        managed = True
        db_table = 'bt_usuarios'
        app_label='main'

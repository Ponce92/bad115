from django.db import models
from django.contrib.auth.models import AbstractUser

from .Roles import Roles

class Users(AbstractUser):
    user_code       = models.CharField(primary_key=True, max_length=8)
    rol_code        = models.ForeignKey(Roles, models.DO_NOTHING, db_column='rol_code', blank=True, null=True)
    username        = models.CharField(unique=True, max_length=150)
    email           = models.CharField(unique=True, max_length=255)
    password        = models.CharField(max_length=255)
    user_attempts   = models.IntegerField(default=0)
    user_state      = models.CharField(max_length=3)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        managed = True
        db_table = 'users'
        app_label='main'
        #app_label define a que aplicacion pertenece
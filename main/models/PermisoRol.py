from django.db import models
from main.models import Rol,Permiso

class PermisoRol(models.Model):
    pk_id = models.AutoField(primary_key=True)
    fk_rol_codigo = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_rol_codigo')
    fk_permiso_codigo = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='fk_permiso_codigo')

    class Meta:
        managed = False
        db_table = 'bt_roles_permisos'
        app_label='main'


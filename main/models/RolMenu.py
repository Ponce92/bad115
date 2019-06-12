from django.db import models
from main.models import Rol,Menu

class RolMenu(models.Model):
    pk_id = models.AutoField(primary_key=True)
    fk_rol_codigo = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_rol_codigo', blank=True, null=False)
    fk_menu_codigo = models.ForeignKey(Menu, models.DO_NOTHING, db_column='fk_menu_codigo', blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'bt_roles_menus'
        app_label='main'

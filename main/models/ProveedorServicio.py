from django.db import models
from main.models import Servicio,Equipo,Proveedor

class ProveedorServicios(models.Model):
    pk_id = models.AutoField(primary_key=True)
    fk_proveedor_codigo = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='fk_proveedor_codigo')
    fk_equipo_codigo = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='fk_equipo_codigo')
    fk_servicio_codigo = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='fk_servicio_codigo')

    class Meta:
        managed = False
        db_table = 'bt_proveedor_servicios'
        app_label = 'main'

from django.db import models

class Servicio(models.Model):
    pk_codigo = models.CharField(primary_key=True, max_length=8)
    ct_nombre = models.CharField(unique=True, max_length=100)
    cd_desc = models.CharField(max_length=8)
    cl_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bt_servicios'
        app_label = 'main'

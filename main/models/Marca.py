from django.db import models


class Marca(models.Model):
    pk_codigo = models.CharField(unique=True, max_length=8, primary_key=True)
    ct_nombre = models.CharField(unique=True, max_length=100)
    cd_desc = models.CharField(max_length=255)
    cl_estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bt_marcas'
        app_label = 'main'

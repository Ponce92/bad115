from django.db import models

class Proveedor(models.Model):
    pk_codigo = models.CharField(primary_key=True, max_length=8)
    ct_nombre = models.CharField(unique=True, max_length=100)
    cd_direc = models.CharField(max_length=255)
    ct_numero_contacto = models.CharField(unique=True, max_length=9)
    ct_responsable = models.CharField(max_length=100)
    ct_email = models.CharField(unique=True, max_length=255)
    ct_nit = models.CharField(unique=True, max_length=100)
    cl_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bt_proveedores'
        app_label = 'main'
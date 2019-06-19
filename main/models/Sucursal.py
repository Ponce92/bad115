from django.db import models

class Sucursal(models.Model):
    pk_codigo = models.CharField(primary_key=True, max_length=8)
    ct_nombre = models.CharField(max_length=8)
    ct_telefono = models.CharField(max_length=9, blank=True, null=True)
    cd_direccion = models.CharField(max_length=255)
    ct_correo = models.CharField(max_length=255)
    cl_estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bt_sucursales'
        app_label='main'

    def __str__(self):
        return '%s' % self.ct_nombre

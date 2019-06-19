from django.db import models

class CategoriaEquipo(models.Model):
    pk_codigo       = models.CharField(primary_key=True, max_length=8)
    ct_nombre       = models.CharField(unique=True, max_length=255)
    cd_descripcion  = models.TextField(max_length=255)
    cl_estado       = models.BooleanField()

    class Meta:
        managed = False
        ordering=['ct_nombre']
        db_table = 'bt_categorias_equipos'
        app_label='main'

    def __str__(self):
        return '%s' % self.ct_nombre
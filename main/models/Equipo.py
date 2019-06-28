from django.db import models
from .CategoriaEquipo import CategoriaEquipo

class Equipo(models.Model):
    pk_codigo = models.CharField(primary_key=True, max_length=8)
    fk_categoria_codigo = models.ForeignKey(CategoriaEquipo, models.DO_NOTHING, db_column='fk_categoria_codigo')
    ct_nombre = models.CharField(unique=True, max_length=150)
    cd_descripcion = models.CharField(max_length=255)
    cl_estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bt_equipos'
        app_label = 'main'


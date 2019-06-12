from django.db import models

class Rol(models.Model):
    pk_codigo       = models.CharField(primary_key=True, max_length=8)
    ct_nombre       = models.CharField(unique=True, max_length=255)
    cd_descripcion  = models.CharField(max_length=255)
    cl_estado       = models.BooleanField()
    cl_editable     = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bt_roles'
        app_label='main'

    def __str__(self):
        return '%s' % self.ct_nombre
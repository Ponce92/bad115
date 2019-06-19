from django.db import models

class Permiso(models.Model):
    '''Modelo e permisos que manejara la aplicacion
    un rol posee ciertos permisos '''
    pk_codigo = models.CharField(primary_key=True, max_length=6)
    ct_nombre = models.CharField(unique=True, max_length=100)
    cd_descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'bt_permisos'
        app_label = 'main'

    def __str__(self):
        return '%s' % self.ct_nombre

from django.db import models

class Menu(models.Model):
    pk_codigo       = models.CharField(primary_key=True, max_length=4)
    fk_menu_codigo  = models.ForeignKey('self', models.DO_NOTHING, db_column='fk_menu_codigo', blank=True, null=True)
    ct_nombre       = models.CharField(unique=True, max_length=150)
    cd_descripcion  = models.CharField(max_length=255)
    cl_estado       = models.CharField(max_length=3)
    ct_url          = models.CharField(max_length=255)
    ct_icono        = models.CharField(max_length=50, null=False)

    class Meta:
        managed   = False
        db_table  = 'bt_menus'
        app_label ='main'

    def __str__(self):
        return '%s' % self.ct_nombre
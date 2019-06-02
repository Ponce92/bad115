from django.db import models

class Roles(models.Model):
    rol_code = models.CharField(primary_key=True, max_length=4)
    rol_name = models.CharField(unique=True, max_length=255)
    rol_desc = models.CharField(max_length=255)
    rol_state = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'roles'
        app_label='main'

from django.db import models


class Cliente(models.Model):
    nro_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=20, default='')

    def __unicode__(self):
        return  self.nombre + " ( " + str(self.nro_cliente) + " )"
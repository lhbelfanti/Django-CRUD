from django.db import models


class Genero(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    def __unicode__(self):
        return self.descripcion

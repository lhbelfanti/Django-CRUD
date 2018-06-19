from django.db import models
from genero import Genero


class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    estreno = models.IntegerField()
    duracion = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=None)

    def __unicode__(self):
        return self.nombre

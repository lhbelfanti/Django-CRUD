from django.db import models
from pelicula import Pelicula
from cliente import Cliente


class Prestamo(models.Model):
    fecha_alquiler = models.DateField()
    fecha_devolucion = models.DateField()
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.pelicula) + " - " + str(self.cliente)

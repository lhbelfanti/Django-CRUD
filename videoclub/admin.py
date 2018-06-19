from django.contrib import admin

from videoclub.models.cliente import Cliente
from videoclub.models.genero import Genero
from videoclub.models.pelicula import Pelicula
from videoclub.models.prestamo import Prestamo

admin.site.register(Cliente)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Prestamo)

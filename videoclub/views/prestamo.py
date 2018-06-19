from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from datetime import datetime

from videoclub.models.cliente import Cliente
from videoclub.models.pelicula import Pelicula
from ..models.prestamo import Prestamo
from django.db.models import Q


class ListaPrestamo(ListView):
    model = Prestamo

    def get_context_data(self, **kwargs):
        context = super(ListaPrestamo, self).get_context_data(**kwargs)
        today = datetime.today()
        context['prestamos'] = Prestamo.objects.filter(Q(fecha_devolucion__gte=today))
        return context


class CrearPrestamo(CreateView):
    model = Prestamo
    fields = [f.name for f in Prestamo._meta.get_fields()]

    def get_context_data(self, **kwargs):
        context = super(CrearPrestamo, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.order_by('estreno')
        context['clientes'] = Cliente.objects.all()
        return context


class ModificarPrestamo(UpdateView):
    model = Prestamo
    fields = [f.name for f in Prestamo._meta.get_fields()]

    def get_context_data(self, **kwargs):
        context = super(ModificarPrestamo, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.order_by('estreno')
        context['clientes'] = Cliente.objects.all()
        return context


class EliminarPrestamo(DeleteView):
    model = Prestamo
    fields = [f.name for f in Prestamo._meta.get_fields()]
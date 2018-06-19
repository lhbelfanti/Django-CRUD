from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from videoclub.models.genero import Genero
from ..models.pelicula import Pelicula


class ListaPelicula(ListView):
    model = Pelicula

    def get_context_data(self, **kwargs):
        context = super(ListaPelicula, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.order_by('estreno')
        return context

class CrearPelicula(CreateView):
    model = Pelicula
    fields = ['nombre', 'estreno', 'duracion', 'genero']

    def get_context_data(self, **kwargs):
        context = super(CrearPelicula, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context

class ModificarPelicula(UpdateView):
    model = Pelicula
    fields = ['nombre', 'estreno', 'duracion', 'genero']

    def get_context_data(self, **kwargs):
        context = super(ModificarPelicula, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context


class EliminarPelicula(DeleteView):
    model = Pelicula
    fields = ['nombre', 'estreno', 'duracion', 'genero']
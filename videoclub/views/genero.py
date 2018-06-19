from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from videoclub.models.pelicula import Pelicula
from ..models.genero import Genero


class ListaGenero(ListView):
    model = Genero

    def get_context_data(self, **kwargs):
        context = super(ListaGenero, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.raw('SELECT codigo, descripcion FROM videoclub_genero g JOIN ( '
                                                'SELECT genero_id, COUNT(*) AS cnt FROM videoclub_pelicula '
                                                'GROUP BY genero_id ) c ON ( genero_id = codigo ) ORDER BY c.cnt DESC')
        return context




class CrearGenero(CreateView):
    model = Genero
    fields = ['codigo', 'descripcion']


class ModificarGenero(UpdateView):
    model = Genero
    fields = ['codigo', 'descripcion']


class EliminarGenero(DeleteView):
    model = Genero
    fields = ['codigo', 'descripcion']
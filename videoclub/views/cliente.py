from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from ..models.cliente import Cliente


class ListaCliente(ListView):
    model = Cliente


class CrearCliente(CreateView):
    model = Cliente
    fields = ['nombre', 'telefono', 'email']


class ModificarCliente(UpdateView):
    model = Cliente
    fields = ['nombre', 'telefono', 'email']


class EliminarCliente(DeleteView):
    model = Cliente
    fields = ['nombre', 'telefono', 'email']
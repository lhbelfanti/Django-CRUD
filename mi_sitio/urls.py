"""mi_sitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView

from videoclub.views.genero import ListaGenero, CrearGenero, ModificarGenero, EliminarGenero
from videoclub.views.cliente import ListaCliente, CrearCliente, ModificarCliente, EliminarCliente
from videoclub.views.pelicula import ListaPelicula, CrearPelicula, ModificarPelicula, EliminarPelicula
from videoclub.views.prestamo import ListaPrestamo, CrearPrestamo, ModificarPrestamo, EliminarPrestamo

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^genero/$', ListaGenero.as_view()),
    url(r'^genero/crear/$', CrearGenero.as_view(success_url="/genero/")),
    url(r'^genero/modificar/(?P<pk>\d+)$', ModificarGenero.as_view(success_url="/genero/")),
    url(r'^genero/eliminar/(?P<pk>\d+)$', EliminarGenero.as_view(success_url="/genero/")),
    url(r'^cliente/$', ListaCliente.as_view()),
    url(r'^cliente/crear/$', CrearCliente.as_view(success_url="/cliente/")),
    url(r'^cliente/modificar/(?P<pk>\d+)$', ModificarCliente.as_view(success_url="/cliente/")),
    url(r'^cliente/eliminar/(?P<pk>\d+)$', EliminarCliente.as_view(success_url="/cliente/")),
    url(r'^pelicula/$', ListaPelicula.as_view()),
    url(r'^pelicula/crear/$', CrearPelicula.as_view(success_url="/pelicula/")),
    url(r'^pelicula/modificar/(?P<pk>\d+)$', ModificarPelicula.as_view(success_url="/pelicula/")),
    url(r'^pelicula/eliminar/(?P<pk>\d+)$', EliminarPelicula.as_view(success_url="/pelicula/")),
    url(r'^prestamo/$', ListaPrestamo.as_view()),
    url(r'^prestamo/crear/$', CrearPrestamo.as_view(success_url="/prestamo/")),
    url(r'^prestamo/modificar/(?P<pk>\d+)$', ModificarPrestamo.as_view(success_url="/prestamo/")),
    url(r'^prestamo/eliminar/(?P<pk>\d+)$', EliminarPrestamo.as_view(success_url="/prestamo/")),
]

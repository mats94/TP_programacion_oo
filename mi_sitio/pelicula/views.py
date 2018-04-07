from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from pelicula.models import Genero


class ListaGenero(ListView):
    model = Genero


class CrearGenero(CreateView):
    model = Genero

    #fields = [f.name for f in Genero._meta.get_fields()]
    fields = ['codigo', 'descripcion']

    print('*' * 50)

    for g in Genero.objects.all():
        print(g)
        

    print('*' * 50)

class ModificarGenero(UpdateView):
    model = Genero
    fields = ['codigo', 'descripcion']


class EliminarGenero(DeleteView):
    model = Genero
    fields = ['codigo', 'descripcion']

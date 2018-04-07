from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from pelicula.models import Genero, Cliente


class ListaGenero(ListView):
    model = Genero


class CrearGenero(CreateView):
    model = Genero

    #fields = [f.name for f in Genero._meta.get_fields()]
    fields = ['codigo', 'descripcion']

    print('*' * 50) # Averiguar

    for g in Genero.objects.all():
        print(g)
        

    print('*' * 50)

class ModificarGenero(UpdateView):
    model = Genero
    fields = ['codigo', 'descripcion']


class EliminarGenero(DeleteView):
    model = Genero
    fields = ['codigo', 'descripcion']

# Agregue
class ListaCliente(ListView):
    model = Cliente

class CrearCliente(CreateView):
    model = Cliente

    fields = ['id', 'nombre' , 'telefono', 'email']

    print('*' * 50)

    for c in Cliente.objects.all():
        print(c)
        
    print('*' * 50)

class ModificarCliente(UpdateView):
    model = Cliente

    fields = ['id', 'nombre' , 'telefono', 'email']


class EliminarCliente(DeleteView):
    model = Cliente

    fields = ['id', 'nombre' , 'telefono', 'email']

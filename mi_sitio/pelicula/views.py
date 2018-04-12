from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from pelicula.models import Genero, Cliente, Prestamo


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


# class ListaPrestamo(ListView):
#   model = Prestamo


#class CrearPrestamo(CreateView):
#    model = Prestamo

#    fields = ['codigoprest', 'fecha' , 'fecha_devolucion', 'pelicula']

#    print('*' * 50)

#    for p in Prestamo.objects.all():
#        print(p)
        
#    print('*' * 50)


#class ModificarPrestamo(UpdateView):
#    model = Prestamo

#    fields = ['codigoprest', 'fecha' , 'fecha_devolucion', 'pelicula']


#class Prestamo(UpdateView):
#    model = Prestamo

#   fields = ['codigoprest', 'fecha' , 'fecha_devolucion', 'pelicula']
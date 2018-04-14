from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from pelicula.models import Genero, Cliente, Prestamo

# Vista de Genero
class ListaGenero(ListView): # Lista los distintos generos de una pelicula (GET)
    model = Genero


class CrearGenero(CreateView): # Crea generos nuevos (POST)
    model = Genero

    fields = ['codigo', 'descripcion']

    print('*' * 50) # Averiguar

    for g in Genero.objects.all():
        print(g)
        
    print('*' * 50)


class ModificarGenero(UpdateView): # Modifica los generos existentes a partir de un ID (PUT)
    model = Genero

    fields = ['codigo', 'descripcion']


class EliminarGenero(DeleteView): # Elimina cualquier genero ee la lista ingresando un ID (DELETE)
    model = Genero
    fields = ['codigo', 'descripcion']


# Vista de cliente
class ListaCliente(ListView): # Lista los distintos clientes que asisten al Videoclub (GET)
    model = Cliente


class CrearCliente(CreateView): # Crea clientes nuevos (POST)
    model = Cliente

    fields = ['id', 'nombre' , 'telefono', 'email']

    print('*' * 50)

    for c in Cliente.objects.all():
        print(c)
        
    print('*' * 50)


class ModificarCliente(UpdateView): # Modifica los datos del cliente a partir de un ID (PUT)
    model = Cliente

    fields = ['id', 'nombre' , 'telefono', 'email']


class EliminarCliente(DeleteView): # Elimina cualquier cliente de la lista ingresando un ID (DELETE)
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
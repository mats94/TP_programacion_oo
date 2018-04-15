from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from pelicula.models import Genero, Cliente, Pelicula






#     --------------              Vista de Genero        ----------------






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


class EliminarGenero(DeleteView): # Elimina cualquier genero de la lista ingresando un ID (DELETE)
    model = Genero
    fields = ['codigo', 'descripcion']





# -----------------------          Vista de cliente   -----------------------






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





# -----------------------------         Vista Pelicula         -----------------------




class ListaPelicula(ListView): # Lista las distintas peliculas que hay en el Videoclub (GET)
    model = Pelicula

    #def something(request):
     #   return render(request, 'pelicula/pelicula_alquilada_list.html')


class CrearPelicula(CreateView): # Crea peliculas nuevas (POST)
    model = Pelicula

    fields =  ['id', 'nombre', 'estreno', 'genero', 'alquilada']

    print('*' * 50)

    for pe in Pelicula.objects.all():
        print(pe)

     
class ModificarPelicula(UpdateView): # Modifica los datos de la pelicula a partir de un ID (PUT)
    model = Pelicula

    fields =  ['id', 'nombre', 'estreno', 'genero', 'alquilada']


class EliminarPelicula(DeleteView): # Elimina cualquier pelicula de la lista ingresando un ID (DELETE)
    model = Pelicula

    fields =  ['nombre', 'estreno', 'genero', 'alquilada']


class BuscarAlquiladaPelicula(ListView): 
    model = Pelicula

    def something(request):
        return render(request, 'pelicula/pelicula_alquilada_list.html')







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
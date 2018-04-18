from django.db import models
from django.views.decorators.http import condition

# Genero de la pelicula
class Genero(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.descripcion

    def saber_codigo(self):
        return self.codigo

# Pelicula
class Pelicula(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estreno = models.DateField(null=True, help_text="Ej: Mes/Dia/Año")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=None)
    alquilada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre    


    def peliculas_alquiladas(self):  # Condicion si la pelicula esta alquilada
       if(self.alquilada == True):
            return self.nombre
       else: 
            return ''

    def peliculas_romanticas(self): # Condicion si la pelicula es romantica
        if(self.genero.codigo == 6):
            return self.nombre
        else:
            return ''    

    def saber_id(self):
        return self.id

# Cliente que asiste al Videoclub
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=20, default='')
  

    def __str__(self):
        return self.nombre
   

# Prestamo de la pelicula
class Prestamo(models.Model):
    codigoprest = models.IntegerField(null=True)
    fecha = models.DateField()
    fecha_devolucion = models.DateField()
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.pelicula


    
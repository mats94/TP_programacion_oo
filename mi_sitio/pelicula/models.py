from django.db import models


class Genero(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.descripcion


class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    estreno = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=None)


class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    fecha = models.DateField()
    fecha_devolucion = models.DateField()
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)



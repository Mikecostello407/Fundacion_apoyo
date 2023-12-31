from django.db import models

# Create your models here.

#Modelo para la Categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCatgoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoría')
    def __str__(self):
        return self.nombreCatgoria

#Modelo para el Vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=25, primary_key=True, verbose_name='Nombre del Medicamento')
    marca = models.CharField(max_length=4, verbose_name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤStock')
    modelo = models.CharField(max_length=10, null=True, verbose_name='ㅤㅤFecha de vencimiento')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    def __str__(self):
        return self.patente

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40) # que tpo de dato (CharField es un caracter corto, por eso 40 caracteres) modelando como va ser el data set en la b en sql
    camada = models.IntegerField()           # inter(entero)  # solo debo determinar las columnas # django crea automaticamente el id bd
    #fecha = models.DateField()
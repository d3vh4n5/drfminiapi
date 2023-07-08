from django.db import models

# Create your models here.

class Verdura(models.Model):
    imagen = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    # id = models.IntegerField() Lo comento porque el id me lo genera por defecto
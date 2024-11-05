from django.db import models

# Create your models here.


class Frutas(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()

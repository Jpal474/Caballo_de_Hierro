from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo=models.TextField()
    resumen=models.TextField()
    fecha=models.DateField()
    autor=models.CharField(max_length=50)
    imagen=models.ImageField()
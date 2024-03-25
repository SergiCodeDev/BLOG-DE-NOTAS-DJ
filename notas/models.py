from django.db import models

# Create your models here.

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo
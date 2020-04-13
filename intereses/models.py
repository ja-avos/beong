from django.db import models

# Create your models here.

class Interes (models.Model):
    class Meta:
        abstract=True

    nombre=models.CharField(max_length=50)



class Gusto(Interes):
    grado=models.CharField(max_length=10)
    def __str__(self):
        return '%s: %s' % (self.nombre, self.grado)


class Idioma(Interes):
    nivel=models.CharField(max_length=10)
    def __str__(self):
        return '%s: %s' % (self.nombre, self.nivel)

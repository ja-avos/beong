from django.db import models

# Create your models here.

class Interes (models.Model):
    class Meta:
        abstract=True

    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)


class Gusto(Interes):
    grado=models.IntegerField()

class Idioma(Interes):
    nivel=models.IntegerField()
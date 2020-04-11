from django.db import models
# Create your models here.


class Usuario (models.Model):
    nombre=models.CharField(max_length=60)
    usuario=models.CharField(max_length=20,primary_key=True)
    contrasenia=models.CharField(max_length=20)

def __str__(self):
    return '%s' % (self.usuario)

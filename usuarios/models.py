from django.db import models
from intereses.models import Gusto,Idioma

class Usuario (models.Model):
    class Meta:
        abstract = True

    nombre=models.CharField(max_length=60, null=False)
    usuario=models.CharField(max_length=20,primary_key=True)
    contrasenia=models.CharField(max_length=20, null=False)

    def __str__(self):
        return '%s' % (self.usuario)

class Administrador (Usuario):
    cargo=models.CharField(max_length=20)

class Voluntario(Usuario):
    descripcion=models.CharField(max_length=200)
    edad=models.IntegerField()
    pais=models.CharField(max_length=25)
    ocupacion=models.CharField(max_length=30)
    idiomas=models.ManyToManyField(Idioma)
    gustos=models.ManyToManyField(Gusto)
    ciudad=models.CharField(max_length=20, blank=True)
    departamento=models.CharField(max_length=20, blank=True)
    imagen = models.CharField(max_length=150, null= True,blank=True)
    correo = models.EmailField(max_length=254, null = True, blank= True)

    def get_class(self):
        return "voluntario"

class ONG(Usuario):
    pais = models.CharField(max_length=25)

    def get_class(self):
        return "ong"




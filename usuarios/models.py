from django.db import models
from intereses.models import Gusto,Idioma
from postulacion.models import Postulacion
from voluntariados.models import Voluntariado
# Create your models here.


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
    descripcion=models.CharField(max_length=100)
    edad=models.IntegerField()
    pais=models.CharField(max_length=25)
    ocupacion=models.CharField(max_length=30)
    idiomas=models.ForeignKey(Idioma, null=False, on_delete=None)
    gustos=models.ForeignKey(Gusto, null=False,on_delete=None)
    postulaciones=models.ForeignKey(Postulacion, on_delete=models.CASCADE)

class ONG(Usuario):
    pais = models.CharField(max_length=25)
    voluntariados= models.ForeignKey(Voluntario,on_delete=None)




from django.db import models


class Postulacion(models.Model):
   # fecha= models.DateField(_("Date"), default=datetime.date.today)
    estado=models.CharField(max_length=20)
    id=models.IntegerField(primary_key=True)

# Create your models here.

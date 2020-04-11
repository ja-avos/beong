from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    email = models.EmailField()
    timeRegistered = models.DateTimeField(timezone.now)

    def __str__(self):
        return self.email + ", time: " + str(self.timeRegistered)
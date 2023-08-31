from django.db import models
from django.contrib.auth.models import User

class Vehicles(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    marca = models.CharField(max_length=15, null=False)
    modelo = models.CharField(max_length=15, null=False)
    ano = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.usuario} - {self.marca} - {self.modelo}'
    
    
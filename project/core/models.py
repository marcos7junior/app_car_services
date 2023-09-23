from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=50)
    dnascimento = models.IntegerField(default=0)
    mascimento = models.CharField(max_length=10, default='null')
    anascimento = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


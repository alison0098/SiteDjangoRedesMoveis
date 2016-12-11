from django.db import models


class Dados(models.Model):
    local = models.CharField(max_length=40)
    data = models.DateTimeField()
    temperatura = models.IntegerField()
    umidade = models.IntegerField()
    presenca = models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.local

class Imagem(models.Model):

    local = models.CharField(max_length=40)
    data = models.DateTimeField()    
    image = models.ImageField(upload_to="polls/static/img")

    def __str__(self):
        return self.image


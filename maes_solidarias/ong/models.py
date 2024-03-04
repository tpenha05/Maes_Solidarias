from django.db import models
from django.contrib.auth.models import User 

# classe responsável pelos dados do usuário doador 

class Campanha(models.Model):
    nome = models.CharField(max_length=50, default='')
    descricao = models.CharField(max_length=250, default='')
    local = models.CharField(max_length=10, default='')
    data_e_horario = models.DateTimeField()
    publico_destinado = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    nome = models.CharField(max_length=50, default='')
    descricao = models.CharField(max_length=250, default='')
    local = models.CharField(max_length=10, default='')
    data_e_horario = models.DateTimeField()
    publico_destinado = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nome
    

from django.db import models
from django.contrib.auth.models import User 

# classe responsável pelos dados do usuário doador 
class Doador(models.Model):
    nome_completo = models.CharField(max_length=100, default='')
    user = models.OneToOneField(User,on_delete=models.CASCADE, default='')
    data_nascimento = models.DateField()
    whatsapp = models.IntegerField()
    email = models.CharField(max_length=100, default='')
    genero = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14)
    forma_de_doacao =  models.CharField(max_length=30)
    periodicidade_doacao = models.CharField(max_length=30)
    valor_doacao = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)


class Evento(models.Model):
    nome = models.CharField(max_length=50, default='')
    descricao = models.CharField(max_length=250, default='')
    local = models.CharField(max_length=10, default='')
    data_e_horario = models.DateTimeField()
    publico_destinado = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nome
    

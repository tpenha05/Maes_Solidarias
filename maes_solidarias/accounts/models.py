from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    nome_completo = models.CharField(max_length=120, null=True, blank=True)
    telefone_celular = models.IntegerField(null=True, blank=True) 
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=120)
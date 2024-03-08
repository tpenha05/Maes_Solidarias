from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.conf import settings



class MyCustomUser(AbstractUser):
    # Adiciona um campo para diferenciar o tipo de usuário
    is_admin = models.BooleanField(default=False)

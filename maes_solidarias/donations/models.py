from django.db import models

class Donation(models.Model):
    
    AMOUNT_CHOICES = [
        (20, 'R$ 20'),
        (50, 'R$ 50'),
        (100, 'R$ 100'),
        ('outro', 'Outro'),
        # Adicione mais opções conforme necessário
    ]
    
    PERIODICITY_CHOICES = [
        ('U', 'Única'),
        ('M', 'Mensal'),
        # Adicione mais opções conforme necessário
    ]

    name = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=15, verbose_name='Telefone', blank=True, null=True)
    birth_date = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    cpf = models.CharField(max_length=11, verbose_name='CPF', unique=True)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, verbose_name='Valor da Doação')
    periodicity = models.CharField(max_length=1, choices=PERIODICITY_CHOICES, verbose_name='Periodicidade')
    donation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data da Doação', choices=AMOUNT_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.amount}'

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'


# Generated by Django 4.1.2 on 2024-03-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('amount', models.IntegerField(choices=[(20, 'R$ 20'), (50, 'R$ 50'), (100, 'R$ 100')], verbose_name='Valor da Doação')),
                ('periodicity', models.CharField(choices=[('U', 'Única'), ('M', 'Mensal')], max_length=1, verbose_name='Periodicidade')),
                ('donation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da Doação')),
            ],
            options={
                'verbose_name': 'Doação',
                'verbose_name_plural': 'Doações',
            },
        ),
    ]

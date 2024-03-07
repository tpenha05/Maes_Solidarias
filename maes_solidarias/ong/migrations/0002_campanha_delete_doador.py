# Generated by Django 4.1.2 on 2024-03-06 17:38
 main

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=50)),
                ('descricao', models.CharField(default='', max_length=250)),
                ('local', models.CharField(default='', max_length=10)),
                ('data_e_horario', models.DateTimeField()),
                ('publico_destinado', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Doador',
        ),
    ]

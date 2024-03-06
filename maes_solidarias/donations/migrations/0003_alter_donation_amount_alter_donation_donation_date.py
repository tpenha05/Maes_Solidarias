# Generated by Django 5.0.2 on 2024-03-06 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_alter_donation_amount_alter_donation_donation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.IntegerField(choices=[(20, 'R$ 20'), (50, 'R$ 50'), (100, 'R$ 100')], verbose_name='Valor da Doação'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da Doação'),
        ),
    ]

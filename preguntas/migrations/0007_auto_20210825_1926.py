# Generated by Django 3.2.5 on 2021-08-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0006_jugador_puntaje_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='puntaje_total',
        ),
        migrations.AddField(
            model_name='jugador',
            name='puntaje_maximo',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-24 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.jugador')),
                ('preguntas', models.ManyToManyField(blank=True, to='preguntas.Pregunta')),
            ],
        ),
        migrations.DeleteModel(
            name='Juego',
        ),
    ]

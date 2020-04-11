# Generated by Django 2.2 on 2020-04-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calificaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('puntuacion', models.IntegerField()),
                ('comentario', models.CharField(max_length=100)),
                ('nombreVoluntario', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Califiacion',
        ),
    ]

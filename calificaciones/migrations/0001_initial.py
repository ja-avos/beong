# Generated by Django 2.2 on 2020-04-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField()),
                ('comentario', models.CharField(max_length=100)),
                ('nombreVoluntario', models.CharField(max_length=50)),
            ],
        ),
    ]

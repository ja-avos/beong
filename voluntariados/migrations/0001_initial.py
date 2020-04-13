

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calificaciones', '0001_initial'),
        ('intereses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voluntariado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=20)),
                ('duracion', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=25)),
                ('precio', models.FloatField()),
                ('imagen', models.CharField(blank=True, max_length=150)),
                ('calificaciones', models.ManyToManyField(blank=True, to='calificaciones.Calificacion')),
                ('gustosRequeridos', models.ManyToManyField(to='intereses.Gusto')),
                ('idiomasRequeridos', models.ManyToManyField(to='intereses.Idioma')),
            ],
        ),
    ]

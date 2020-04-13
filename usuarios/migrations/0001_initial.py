

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postulacion', '0001_initial'),
        ('intereses', '0001_initial'),
        ('voluntariados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('nombre', models.CharField(max_length=60)),
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=20)),
                ('cargo', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('nombre', models.CharField(max_length=60)),
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('pais', models.CharField(max_length=25)),
                ('ocupacion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(blank=True, max_length=20)),
                ('departamento', models.CharField(blank=True, max_length=20)),
                ('imagen', models.CharField(blank=True, max_length=150)),
                ('gustos', models.ManyToManyField(to='intereses.Gusto')),
                ('idiomas', models.ManyToManyField(to='intereses.Idioma')),
                ('postulaciones', models.ManyToManyField(blank=True, to='postulacion.Postulacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ONG',
            fields=[
                ('nombre', models.CharField(max_length=60)),
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=25)),
                ('ocupacion', models.CharField(max_length=30)),
                ('gustos', models.ManyToManyField(to='intereses.Gusto')),
                ('idiomas', models.ManyToManyField(to='intereses.Idioma')),
                ('postulaciones', models.ManyToManyField(to='postulacion.Postulacion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

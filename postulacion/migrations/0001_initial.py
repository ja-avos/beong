
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voluntariados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('voluntariado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='voluntariados.Voluntariado')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2020-04-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voluntario',
            name='correo',
            field=models.EmailField(default='efe@hotmai.com', max_length=254),
        ),
    ]

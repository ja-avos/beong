# Generated by Django 2.2 on 2020-04-12 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intereses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gusto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
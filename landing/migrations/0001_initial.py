# Generated by Django 3.0.4 on 2020-04-12 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('timeRegistered', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='puntuacion',
            field=models.PositiveIntegerField(default=5),
        ),
    ]

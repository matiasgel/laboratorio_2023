# Generated by Django 4.2 on 2023-04-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_alter_autor_fecha_nacimiento_alter_libro_anio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='libro',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ManyToManyField(to='libreria.autor'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libreria", "0007_remove_autor_libro_libro_autor"),
    ]

    operations = [
        migrations.AddField(
            model_name="autor",
            name="foto",
            field=models.ImageField(default="nofoto.jpg", upload_to="autores"),
        ),
    ]
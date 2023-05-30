# Generated by Django 4.2 on 2023-04-19 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_alter_libro_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_estado', models.CharField(choices=[('PRESTADA', 'Prestada'), ('BIBLIOTECA', 'En biblioteca'), ('RETRASO', 'Retraso'), ('REPARACION', 'Repatración')], default='BIBLIOTECA', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_lector', models.CharField(choices=[('HABILITADO', 'Habilitado'), ('MULTADO', 'Multado')], default='HABILITADO', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='libro',
            field=models.ManyToManyField(to='libreria.libro'),
        ),
        migrations.AddField(
            model_name='libro',
            name='tipo_libro',
            field=models.CharField(choices=[('NOVELA', 'Novela'), ('TEATRO', 'Teatro'), ('POESIA', 'Poesía'), ('ENSAYO', 'Ensayo')], default='POESIA', max_length=20),
        ),
    ]

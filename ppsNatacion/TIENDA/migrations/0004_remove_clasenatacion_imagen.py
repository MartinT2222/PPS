# Generated by Django 4.0.1 on 2024-01-10 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDA', '0003_clasenatacion_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clasenatacion',
            name='imagen',
        ),
    ]
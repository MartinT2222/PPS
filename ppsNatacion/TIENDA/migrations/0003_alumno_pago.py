# Generated by Django 4.2.1 on 2023-10-19 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDA', '0002_remove_alumno_id_alter_alumno_alumno_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='pago',
            field=models.BooleanField(default=False),
        ),
    ]
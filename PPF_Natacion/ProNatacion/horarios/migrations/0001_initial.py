# Generated by Django 4.0.1 on 2023-10-05 00:05

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('clase_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField(default=datetime.time(23, 59, 59))),
            ],
        ),
        migrations.CreateModel(
            name='HorarioClase',
            fields=[
                ('horario_id', models.AutoField(primary_key=True, serialize=False)),
                ('dia_semana', models.CharField(max_length=20)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
    ]

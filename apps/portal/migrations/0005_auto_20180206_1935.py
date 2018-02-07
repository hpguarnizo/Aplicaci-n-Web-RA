# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-07 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_remove_carrera_carrera_asignatura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurso',
            name='id',
        ),
        migrations.AddField(
            model_name='asignatura',
            name='id_carrera',
            field=models.ForeignKey(db_column='id_carrera', default='', on_delete=django.db.models.deletion.CASCADE, to='portal.Carrera'),
        ),
        migrations.AddField(
            model_name='recurso',
            name='id_asignatura',
            field=models.ForeignKey(db_column='id_asignatura', default='', on_delete=django.db.models.deletion.CASCADE, to='portal.Asignatura'),
        ),
        migrations.AddField(
            model_name='recurso',
            name='id_recurso',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo_recurso',
            field=models.CharField(choices=[('Imagen', 'Imagen'), ('Video', 'Video'), ('3D', '3D'), ('PDF', 'PDF'), ('MP3', 'MP3')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]

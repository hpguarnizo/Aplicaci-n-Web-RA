# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-07 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='archivo_recurso',
            field=models.FileField(default='', upload_to=''),
        ),
    ]

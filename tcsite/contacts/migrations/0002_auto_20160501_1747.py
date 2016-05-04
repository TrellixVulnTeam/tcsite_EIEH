# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='longitude',
        ),
        migrations.AddField(
            model_name='contacts',
            name='adress',
            field=models.CharField(default=0, max_length=100, verbose_name='adress'),
            preserve_default=False,
        ),
    ]

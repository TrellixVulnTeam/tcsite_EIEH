# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 18:00
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160511_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottom',
            name='blockquote',
        ),
        migrations.RemoveField(
            model_name='bottom',
            name='cite',
        ),
        migrations.RemoveField(
            model_name='bottom',
            name='h1',
        ),
        migrations.RemoveField(
            model_name='bottom',
            name='h2',
        ),
        migrations.RemoveField(
            model_name='bottom',
            name='h3',
        ),
        migrations.AlterField(
            model_name='bottom',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/block', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='bottom',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='bottom',
            name='video',
            field=models.CharField(blank=True, max_length=35, verbose_name='Видео ID(youtube)'),
        ),
        migrations.AlterField(
            model_name='top',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/block', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='top',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='top',
            name='video',
            field=models.CharField(blank=True, max_length=35, verbose_name='Видео ID(youtube)'),
        ),
    ]

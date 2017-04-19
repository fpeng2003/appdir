# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 22:03
from __future__ import unicode_literals

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=app.models.article_img_upload),
        ),
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, upload_to=app.models.info_img_upload),
        ),
    ]

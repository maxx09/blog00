# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0003_auto_20180718_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subTitle',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-20 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='immiuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='immiuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

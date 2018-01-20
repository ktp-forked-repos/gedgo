# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-20 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gedgo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='thumb',
        ),
        migrations.AddField(
            model_name='family',
            name='last_changed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_changed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=b'gedcom'),
        ),
    ]

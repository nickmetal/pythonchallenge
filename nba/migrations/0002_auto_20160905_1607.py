# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='nane',
            new_name='name',
        ),
    ]

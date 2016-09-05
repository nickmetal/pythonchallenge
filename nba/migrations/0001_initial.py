# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nane', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('experience', models.PositiveIntegerField()),
                ('goals', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba.Team'),
        ),
    ]

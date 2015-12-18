# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 03:25
from __future__ import unicode_literals

import counters_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_hash', models.BigIntegerField(default=0)),
                ('app_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_hash', models.BigIntegerField(default=0)),
                ('app_name', models.CharField(max_length=100)),
                ('counter_name', models.CharField(max_length=200)),
                ('counter_value', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='url_hash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_hash', models.BigIntegerField(default=counters_app.models.uniqueid)),
            ],
        ),
    ]

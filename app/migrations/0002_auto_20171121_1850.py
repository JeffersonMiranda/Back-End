# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='idUser',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
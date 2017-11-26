# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171122_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('idUser', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nameUserProfile', models.CharField(max_length=20)),
                ('genderUserProfile', models.SmallIntegerField()),
                ('ageUserProfile', models.CharField(max_length=2)),
                ('statusUserProfile', models.CharField(max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='nameUser',
        ),
        migrations.AddField(
            model_name='users',
            name='createdAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='updateAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='UserProfile_idUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
    ]
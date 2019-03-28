# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-28 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tedix_ro', '0005_auto_20190328_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentprofile',
            name='password',
            field=models.CharField(default='test', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructorprofile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parentprofile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='neighbourhood',
        ),
    ]

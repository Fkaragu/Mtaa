# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_comment_neighbourhood'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Neigh_name',
            new_name='NeighName',
        ),
    ]
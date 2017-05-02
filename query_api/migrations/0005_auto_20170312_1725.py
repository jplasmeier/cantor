# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_api', '0004_auto_20170312_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queryobject',
            name='next_query',
        ),
        migrations.AddField(
            model_name='queryobject',
            name='next_query',
            field=models.ManyToManyField(related_name='_queryobject_next_query_+', to='query_api.QueryObject'),
        ),
    ]

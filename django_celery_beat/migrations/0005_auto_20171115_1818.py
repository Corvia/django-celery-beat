# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0004_auto_20170221_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='headers',
            field=models.TextField(blank=True, default='{}', help_text='JSON encoded message headers', null=True, verbose_name='Message headers'),
        ),
    ]

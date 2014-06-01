# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bodytracker', '0002_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distanceactivity',
            name='distance',
            field=models.PositiveIntegerField(blank=True, null=True, help_text='Distance in meters'),
        ),
        migrations.AlterField(
            model_name='distanceactivity',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True, help_text='Duration in seconds'),
        ),
    ]

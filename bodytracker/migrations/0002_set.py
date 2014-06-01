# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bodytracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('reps', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('activity', models.ForeignKey(to_field='activity_ptr', to='bodytracker.RepetitionActivity')),
                ('_order', models.OrderWrt()),
            ],
            options={
                'order_with_respect_to': 'activity',
            },
            bases=(models.Model,),
        ),
    ]

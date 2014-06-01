# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDefinition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('activity_type', models.CharField(max_length=100, choices=[('RepetitionActivity', 'Repetition'), ('DistanceActivity', 'Distance')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('body_fat', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('when', models.DateTimeField()),
                ('finished', models.BooleanField(default=False)),
                ('calories', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeightEntry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('body_fat', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivitySet',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('activities', models.ManyToManyField(to='bodytracker.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DistanceActivity',
            fields=[
                ('activity_ptr', models.OneToOneField(to_field='id', to='bodytracker.Activity', auto_created=True, serialize=False, primary_key=True)),
                ('distance', models.PositiveIntegerField(help_text='Distance in meters')),
                ('duration', models.PositiveIntegerField(help_text='Duration in seconds')),
            ],
            options={
            },
            bases=('bodytracker.activity',),
        ),
        migrations.CreateModel(
            name='RepetitionActivity',
            fields=[
                ('activity_ptr', models.OneToOneField(to_field='id', to='bodytracker.Activity', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=('bodytracker.activity',),
        ),
    ]

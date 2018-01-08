# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-08 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0072_auto_20180108_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservationWellStatus',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30, null=True)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('observation_well_status_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_observation_well_status',
                'ordering': ['sort_order', 'code'],
            },
        ),
        migrations.AlterField(
            model_name='well',
            name='observation_well_status',
            field=models.ForeignKey(blank=True, db_column='observation_well_status_guid', null='True', on_delete=django.db.models.deletion.CASCADE, to='gwells.ObservationWellStatus', verbose_name='Observation Well Status'),
        ),
    ]

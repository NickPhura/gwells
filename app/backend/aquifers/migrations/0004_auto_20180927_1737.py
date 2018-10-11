# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-27 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aquifers', '0003_auto_20180924_2205'),
        ('wells', '0021_delete_aquifervulnerabilitycode')
    ]

    operations = [
        migrations.CreateModel(
            name='AquiferVulnerabilityCode',
            fields=[
                ('create_user', models.CharField(max_length=60)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(max_length=60, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(db_column='aquifer_vulnerability_code', max_length=1, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('display_order', models.PositiveIntegerField()),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Aquifer Vulnerability Codes',
                'db_table': 'aquifer_vulnerability_code',
                'ordering': ['display_order', 'code'],
            },
        ),
        migrations.AddField(
            model_name='aquifer',
            name='vulnerability',
            field=models.ForeignKey(blank=True, db_column='aquifer_vulnerablity_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='aquifers.AquiferVulnerabilityCode', verbose_name='Aquifer Vulnerabiliy'),
        ),
    ]
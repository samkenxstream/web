# Generated by Django 2.1.4 on 2018-12-26 17:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConversionRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('from_amount', models.FloatField()),
                ('to_amount', models.FloatField()),
                ('timestamp', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('source', models.CharField(db_index=True, max_length=30)),
                ('from_currency', models.CharField(db_index=True, max_length=30)),
                ('to_currency', models.CharField(db_index=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('address', models.CharField(db_index=True, max_length=255)),
                ('symbol', models.CharField(db_index=True, max_length=10)),
                ('network', models.CharField(db_index=True, max_length=25)),
                ('decimals', models.IntegerField(default=18)),
                ('priority', models.IntegerField(default=1)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('approved', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
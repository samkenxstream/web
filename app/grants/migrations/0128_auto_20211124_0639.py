# Generated by Django 2.2.24 on 2021-11-24 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0127_auto_20211029_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grantcollection',
            options={'get_latest_by': 'created_on'},
        ),
    ]
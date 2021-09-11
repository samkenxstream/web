# Generated by Django 2.2.24 on 2021-09-09 13:31

from django.db import migrations, models
import django.db.models.deletion
import economy.models
import grants.utils


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0122_create_trigger'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrantHallOfFame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('total_donations', models.CharField(help_text='The total donations', max_length=25)),
                ('top_matching_partners', models.ImageField(help_text='The image with the top matching partners (recommended size 1114x390)', upload_to=grants.utils.get_upload_filename)),
                ('top_individual_donors', models.ImageField(help_text='The image with the top individual donors (recommended size 1114x346)', upload_to=grants.utils.get_upload_filename)),
                ('graduated_grantees_description', models.TextField(blank=True, help_text='Short description for graduated grantees')),
                ('share_your_story_email', models.CharField(help_text='The email where users can share their stories', max_length=100)),
                ('is_published', models.BooleanField(default=False, help_text='True if this page is published. Only 1 object can be set to true at a given time.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GrantHallOfFameGrantee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('logo', models.ImageField(help_text='Grantee logo (recommended size 125x125)', upload_to=grants.utils.get_upload_filename)),
                ('username', models.CharField(help_text='Username', max_length=100)),
                ('name', models.CharField(help_text='Name', max_length=100)),
                ('funded_by', models.CharField(help_text='Funded by ...', max_length=100)),
                ('amount', models.CharField(help_text='The amount that has been rased', max_length=20)),
                ('description', models.TextField(help_text='Project description')),
                ('accomplishment_1', models.TextField(blank=True, help_text='Accomplishment 1')),
                ('accomplishment_2', models.TextField(blank=True, help_text='Accomplishment 2')),
                ('hall_of_fame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grantees', to='grants.GrantHallOfFame')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
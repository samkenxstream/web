# Generated by Django 2.2.24 on 2021-10-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0125_auto_20210928_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantclr',
            name='claim_end_date',
            field=models.DateTimeField(blank=True, help_text='CLR Claim End Date', null=True),
        ),
        migrations.AddField(
            model_name='grantclr',
            name='claim_start_date',
            field=models.DateTimeField(blank=True, help_text='CLR Claim Start Date', null=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='checkout_type',
            field=models.CharField(blank=True, choices=[('eth_std', 'eth_std'), ('eth_zksync', 'eth_zksync'), ('eth_polygon', 'eth_polygon'), ('zcash_std', 'zcash_std'), ('celo_std', 'celo_std'), ('zil_std', 'zil_std'), ('polkadot_std', 'polkadot_std'), ('harmony_std', 'harmony_std'), ('binance_std', 'binance_std'), ('rsk_std', 'rsk_std'), ('algorand_std', 'algorand_std')], help_text='The checkout method used while making the contribution', max_length=30, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-25 18:34

from django.db import migrations, models

import config.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="wallet_address",
            field=models.CharField(
                db_index=True,
                max_length=100,
                null=True,
                unique=True,
                validators=[config.helpers.is_valid_wallet_address],
                verbose_name="Wallet address",
            ),
        ),
    ]
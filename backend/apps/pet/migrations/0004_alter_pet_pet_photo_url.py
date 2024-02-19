# Generated by Django 5.0.1 on 2024-02-19 06:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0003_pet_pet_key_pet_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="pet_photo_url",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["png", "jpg", "jpeg"]
                    )
                ],
                verbose_name="Pet photo",
            ),
        ),
    ]

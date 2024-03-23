# Generated by Django 5.0.1 on 2024-03-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_customuser_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                max_length=100, null=True, unique=True, verbose_name="Username"
            ),
        ),
    ]

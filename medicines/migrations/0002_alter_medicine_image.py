# Generated by Django 4.2.7 on 2023-11-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicine",
            name="image",
            field=models.ImageField(
                blank=True, default="default.png", null=True, upload_to="images/"
            ),
        ),
    ]
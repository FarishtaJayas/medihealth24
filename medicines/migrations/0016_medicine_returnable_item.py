# Generated by Django 4.2.7 on 2023-12-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0015_alter_medicine_prescription_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicine",
            name="returnable_item",
            field=models.BooleanField(default=True),
        ),
    ]

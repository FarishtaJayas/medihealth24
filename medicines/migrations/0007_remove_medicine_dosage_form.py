# Generated by Django 4.2.7 on 2023-11-26 19:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0006_medicinetype_medicine_express_delivery_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicine",
            name="dosage_form",
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0013_alter_manufacturer_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manufacturer",
            name="name",
            field=models.CharField(max_length=250),
        ),
    ]

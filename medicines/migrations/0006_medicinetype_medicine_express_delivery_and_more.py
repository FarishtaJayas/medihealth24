# Generated by Django 4.2.7 on 2023-11-26 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0005_alter_category_image_alter_medicine_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicineType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=250, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="medicine",
            name="express_delivery",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="medicine",
            name="medicine_type",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="medicines.medicinetype",
            ),
        ),
    ]

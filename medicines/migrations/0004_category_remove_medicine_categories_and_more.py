# Generated by Django 4.2.7 on 2023-11-25 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0003_medicine_created_alter_medicine_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=250)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="static/images/category_images/",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="medicine",
            name="categories",
        ),
        migrations.AddField(
            model_name="medicine",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="medicines.category",
            ),
        ),
    ]

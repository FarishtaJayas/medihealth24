# Generated by Django 4.2.8 on 2024-01-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0018_remove_medicine_refrigerated'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='refrigerated',
            field=models.BooleanField(default=False),
        ),
    ]

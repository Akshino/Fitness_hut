# Generated by Django 4.2.5 on 2024-09-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitness_app", "0002_product_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.CharField(default="", max_length=255),
        ),
    ]

# Generated by Django 5.1 on 2024-09-18 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_manufactured_at_alter_product_update_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductVersion",
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
                (
                    "version",
                    models.PositiveIntegerField(verbose_name="Версия продукта"),
                ),
                (
                    "name_version",
                    models.CharField(max_length=128, verbose_name="Название версии"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False, verbose_name="Признак текущей версии"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]

from django.db import models

from blog.models import NULLABLE
from config import settings


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="name")
    description = models.CharField(max_length=64, verbose_name="description")

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Categy"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name="name")
    description = models.CharField(max_length=64, verbose_name="description")
    image = models.ImageField(upload_to="media/catalog", verbose_name="image")
    price = models.IntegerField(verbose_name="price")
    created_at = models.DateField(verbose_name="created", auto_now_add=True)
    update_at = models.DateField(verbose_name="updated", auto_now=True)
    manufactured_at = models.DateField(verbose_name="manufactured", auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name="active")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="category"
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')


    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        permissions = [
            ('editing_is_active', 'Can edit is_active'),
            ('editing_description', 'Can edit description'),
            ('editing_category', 'Can edit category'),
        ]

    def __str__(self):
        return self.name

class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version = models.PositiveIntegerField(verbose_name='Версия продукта')
    name_version = models.CharField(max_length=128, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    def __str__(self):
        return f"{self.product} ({self.version})"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
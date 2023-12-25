from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    avatar = models.ImageField(upload_to='media/profiles')


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Наименование товара/услуги')
    description = models.TextField(max_length=1000, verbose_name='Описание товара/услуги')
    image = models.ImageField(upload_to='media/products', verbose_name='Изображение')

    types = (
        ('Услуга', 'Услуга'),
        ('Товар', 'Товар')
    )

    type = models.CharField(max_length=6, choices=types, verbose_name='Выберите, услуга это или товар')


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Заказанный товар')
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    order_date = models.DateTimeField(auto_now_add=True)

# Create your models here.

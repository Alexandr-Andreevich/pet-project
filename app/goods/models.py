from django.db import models

import json


# models - таблицы


class Categories(models.Model):  # наследуемся от класса Model, который находится в пакете models
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Название')  # unique - каждое имя должно быть уникальным
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True,
                            verbose_name='URL')  # blank - поле может быть пустым. Null - связанный с ним параметр

    # класс Meta - задаем имя таблицы
    class Meta:
        db_table = 'category'  # название таблицы в базе данных
        verbose_name = 'Категорию'  # альтернативное имя для отображения в админ панеле (ед.число)
        verbose_name_plural = 'Категории'  # альтернативное имя для отображения в админ панеле (множ.число)
        ordering = ('id',)  # По какому полю сортировка

    # выводим понятные названия категорий в админ панеле
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, )
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}, Количество - {self.quantity}, Цена - {self.price}, Категория - {self.category}'

    def calculation_discount(self):
        # float_discount = self.discount / 100
        # deductible = self.price * float_discount
        # current_discounted_price = self.price - deductible
        # return round(current_discounted_price,2)
            # или так
        if (self.discount):
            # current_discounted_price = round(self.price - self.price * self.discount / 100, 2) # round(... , 2) - округляем до второго знака после запятой
            return round(self.price - self.price * self.discount / 100, 2)
        else:
            return self.price
    

    def id_on_page_product(self):
        return f'{self.id:05}'
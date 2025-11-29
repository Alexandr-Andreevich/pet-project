from django.db import models
from users.models import User
from goods.models import Products


class CartQuerySet(models.QuerySet):

    def total_price(self): # метод возвращает стоимость ВСЕХ товаров в корзине
        return sum(cart.product_price() for cart in self)
    
    def total_quantity(self): # метод возвращает колличество ВСЕХ товаров в корзине
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь') # blank=True, null=True - если пользователя нет (не зарегистрирован),
                                                                                                                                             # поле будет пустым
    session_key = models.CharField(max_length=32, null=True, blank=True) # каждому пользователю, Django присваевает уникальный ключ сессии. Потом из сессии при регистрации
                                                                                                # все перекидывается на зарегистрированного пользователя
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta: # Отображение в админке
        db_table = 'cart'
        verbose_name='Корзину'
        verbose_name_plural='Корзина'

    objects = CartQuerySet().as_manager() # переопределяем Manager objects

    def product_price(self): # метод возвращает стоимость товара в корзине
        return round(self.product.calculation_discount() * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.user} | Товар {self.product.name} | Количество {self.quantity}'
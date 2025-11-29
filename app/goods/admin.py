from django.contrib import admin

from goods.models import Categories, Products

# регистрация моделей(таблиц)

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)  # декорируем класс через пакет @admin декоратор register передавая модель (Categories)
class CategoriesAdmin(admin.ModelAdmin):  # наследуемся от ModelAdmin
    prepopulated_fields = {'slug': ('name',)}  # переменная для автоматического заполнения полей
    # переменная = {'поле для автоматического заполнения': ('поле с которого берем образец названия')}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
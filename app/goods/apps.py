from django.apps import AppConfig
# apps - название раздела таблиц


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    verbose_name = 'Товары'

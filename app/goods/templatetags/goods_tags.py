from django import template
from django.utils.http import urlencode
from goods.models import Categories

# регистрируем шаблонный тег pop_up_menu
register = template.Library() # экземпляр класса Librery переменная register - это специальный декоратор

@register.simple_tag() # через метод simple_tag регистрируем простой тег. Теперь по имени функции в шаблоне можно получить результат функции
def pop_up_menu():
    return Categories.objects.all()


 # takes_context=True - все контекстные переменные ( context = {...} ) (из views.py) и
 # параметр request из шаблона будут доступны через параметр context в функции change_params
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs): # **kwargs - в этот параметр попадают все именованные аргументы из GET запроса, и находятся в виде словаря
    # из context['request'].GET.dict() - получаем все параметры GET запроса со страницы которая уже была открыта (выбраны пользовательские фильтры)
    query = context['request'].GET.dict() 
    # query.update(kwargs) - в словарь query добавляем данные (kwargs) о странице которую нужно открыть
    query.update(kwargs)
    # urlencode - функция которая формирует из словаря key:value, и возвращает готовую строку которую можно использовать как параметры в URL адресе
    return urlencode(query) 
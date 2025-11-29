from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):

    context = {
        'title': 'Главная страница',
        'content': 'Добро пожаловать в магазин мебели!',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Страница о нас',
        'content': 'Добро пожаловать. Эта страница о нас',
        'text_on_page': 'В нашем мебельном магазине вы найдёте '
                        'широкий выбор стильной и функциональной '
                        'мебели по доступным ценам. Мы предлагаем '
                        'удобные системы для любой комнаты — от спальни '
                        'до гостиной. Приходите и выбирайте свою идеальную мебель!'
    }
    return render(request, 'main/about.html', context)

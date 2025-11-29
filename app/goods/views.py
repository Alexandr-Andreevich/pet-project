from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.shortcuts import get_list_or_404, render
from goods.utils import q_search
from goods.models import Products


def catalog(request, categories_slug=None):
    query = request.GET.get('q', None)
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by= request.GET.get('order_by', None)

    # !!! вся фильтрация работает через команды базы данных !!!
    # !!! все проверки на фильры суммируются, и выдаются одним запросом !!!
    if categories_slug == 'vse-tovary':
        arrayGoods = Products.objects.all()
    elif query:
        arrayGoods = q_search(query)
    else:
        arrayGoods = get_list_or_404(Products.objects.filter(category__slug=categories_slug))

    if on_sale:
        arrayGoods = arrayGoods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        arrayGoods = arrayGoods.order_by(order_by)

    paginator = Paginator(arrayGoods, 3)
    current_page = paginator.page(int(page))
    
    context = {
        'title': 'Каталог товаров',
        'goods': current_page,
        'slug_url': categories_slug,
    }
    # {{goods.object_list.index.parametr}} - обращение к списку элементов через объект класса Paginator на странице шаблона
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, 'goods/product.html', context)

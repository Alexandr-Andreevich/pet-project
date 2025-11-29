
from re import search
from django.db.models import Q
from goods.models import Products
from django.contrib.postgres.search import (SearchVector, SearchQuery, SearchRank, SearchHeadline)

# search - полнотекстовый поиск по одному полю Таблицы БД
# SearchVector - полнотекстовый поиск по двум полям Таблицы БД
# SearchQuery - преобразует введенные пользователем термины в объект поискового запроса, который база данных сравнивает с поисковым вектором
# SearchRank - поиск по наибольшему совпадению запроса

def q_search(query):
    
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
#--------------------------------------------------------- Вариант 4 - Полнотекстовый поиск с выделением текста -------------------------------------------------
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects
        .annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline = SearchHeadline(
            'name',
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )

    result = result.annotate(
        bodyline = SearchHeadline(
            'description',
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )

    return result

#--------------------------------------------------------- Вариант 3 - Полнотекстовый поиск --------------------------------------------------------------------

    # return Products.objects.annotate(search=SearchVector("name", "description")).filter(search=query)

#--------------------------------------------------------- Вариант 2 - Стандартный поиск в Django --------------------------------------------------------------

    # return Products.objects.filter(description__search=query )

#--------------------------------------------------------- Вариант 1 - Свой поиск ------------------------------------------------------------------------------

    # arrayWords = [words for words in query.split() if len(words) > 2] 

    # q_objects = Q()

    # for token in arrayWords:
    #     q_objects |= Q(name__icontains=token) # Фильтр icontains это оператор, который осуществляет поиск подстроки без учёта регистра.
    #     q_objects |= Q(description__icontains=token)

    # return Products.objects.filter(q_objects)
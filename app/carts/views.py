from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.utils import get_user_cart
from carts.models import Cart
from goods.models import Products

# Create your views here.
# def cart_add(request):

#     product_id = request.POST.get('product_id')
#     product = Products.objects.get(id=product_id)
    
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user, product=product)

#         if cart.exists(): # если карзина .exist() - существует
#             element = cart.first() # берем .first() - первый элемент корзины
#             if element:
#                 element.quantity += 1
#                 element.save()
#         else:
#             Cart.objects.create(user=request.user, product=product, quantity=1)

#     else:
#         cart = Cart.objects.filter(session_key=request.session.session_key, product=product)
        
#         if cart.exists():
#             element = cart.first()
#             if element:
#                 element.quantity += 1
#                 element.save()
#         else:
#             Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

#     user_carts = get_user_cart(request)
#     cart_items_html = render_to_string(
#         "carts/includes/include_cart.html", {"carts": user_carts}, request=request)

#     response_data = {
#         "message": 'Товар добавлен в корзину',
#         "cart_items_html": cart_items_html,
#     }

#     # return redirect(request.META['HTTP_REFERER']) # в параметре request, в атрибуте META, есть ключ HTTP_REFERER. Он отвечает за то, с какой страницы пользователь зашел в контроллер
#     return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    new_quantity = request.POST.get('quantity')
    
    cart = Cart.objects.get(id=cart_id)
    cart.quantity = new_quantity
    cart.save()

    user_carts = get_user_cart(request)
    cart_items_html = render_to_string(
        "carts/includes/include_cart.html", {"carts": user_carts}, request=request)
    
    response_data = {
        "message": "Колличество товаров изменено",
        "cart_items_html": cart_items_html,
        # "quantity": new_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):

    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity    
    cart.delete()

    user_carts = get_user_cart(request) # user_carts - нужен для того, что бы отрисовать все корзины пользователя в шаблоне
    cart_items_html = render_to_string(
        "carts/includes/include_cart.html", {"carts": user_carts}, request=request)
    
    response_data = {
        "message": "Товар был удален из корзины",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
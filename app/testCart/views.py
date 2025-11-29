from genericpath import exists
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from carts.utils import get_user_cart
from carts.models import Cart
from goods.models import Products


def addCart(request):
    product_id = request.POST.get('product_id')
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)
        
        if cart.exists():
            element = cart.first()
            element.quantity += 1
            element.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = Cart.objects.filter(session_key=request.session.session_key, product=product)

        if cart.exists():
            element = cart.first()
            element.quantity += 1
            element.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    userCarts = get_user_cart(request)
    cart_items_html = render_to_string(
        'testCart/includes/items_cart.html', {'carts': userCarts}, request=request
    )

    context = {
        'cart_items_html': cart_items_html,
    }

    return JsonResponse(context)


def changeCart(request):
    quantity = request.POST.get('quantity')
    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()

    userCarts = get_user_cart(request)
    cart_items_html = render_to_string(
        'testCart/includes/items_cart.html', {'carts': userCarts}, request=request
    )

    context = {
        'cart_items_html': cart_items_html,
    }

    return JsonResponse(context)

def removeCart(request):
    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    quantity_deleted = cart.quantity

    cart.delete()

    userCarts = get_user_cart(request)
    cart_items_html = render_to_string(
        'testCart/includes/items_cart.html', {'carts': userCarts}, request=request
    )

    context = {
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity_deleted
    }

    return JsonResponse(context)
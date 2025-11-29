from email import message
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import UserFormLogin, userFormRegistration, userFormProfile
from django.contrib.auth.decorators import login_required
from carts.models import Cart


def login(request):
    if request.method == "POST":
        form = UserFormLogin(data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = auth.authenticate(username=username, password=password)
            
            session_key = request.session.session_key
            
            if user:
                auth.login(request, user)
                messages.success(request, f"{username} Вы вошли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)


                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserFormLogin()

    context = {
        "title": "Авторизация",
        "form": form,
    }
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = userFormRegistration(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(reverse("user:login"))
    else:
        form = userFormRegistration()

    context = {
        "title": "Регистрация",
        "form": form,
    }
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = userFormProfile(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = userFormProfile(instance=request.user)

    context = {
        "title": "Кабинет",
        "form": form,
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))


def user_cart(request):
    return render(request, 'users/user-cart.html')
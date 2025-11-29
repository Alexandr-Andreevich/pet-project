from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# AuthenticationForm — встроенный класс формы в Django для обработки данных аутентификации (входа пользователя).
from users.models import User

class UserFormLogin(AuthenticationForm):

# если нет стилей на фронте, добавляем тут в backend
    # username = forms.CharField(
    #     label='Имя пользователя',
    #     widget=forms.TextInput(attrs={
    #         'autofocus': True,
    #         'class': 'form-control',
    #         "placeholder": 'Введиме имя пользователя',
    #     })
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={
    #         'autocomplete': 'current-password',
    #         'class': 'form-control',
    #         "placeholder": 'Введиме ваш пароль',
    #     })
    # )
    
    class Meta:
        model = User
        fields = ('username', 'password')

class userFormRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class userFormProfile(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    image = forms.ImageField(required=False)
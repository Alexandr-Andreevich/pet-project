from django.contrib import admin
from users.models import User

# регистрация моделей(таблиц)

admin.site.register(User)
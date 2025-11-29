# 🛍 Pet-project - Интернет-магазин (Django)

## 🚀 Запуск проекта

### 1. Локальный запуск

1. Установите зависимости:
```bash
python -m pip install -r requirements.txt
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
venv\Scripts\activate    # Windows
```

3. Запустите миграции:
```bash
python manage.py migrate
```

4. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

5. Загрузите копии данных:
```bash
py manage.py loaddata fixtures/goods/categorii.json
py manage.py loaddata fixtures/goods/producti.json
```

6. Запустите сервер:
```bash
python manage.py runserver
```

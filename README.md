# 🛍 Pet-project - Интернет-магазин (Django)

## 🚀 Запуск проекта

### 1. Локальный запуск

# Клонируйте репозиторий
```git clone https://github.com/Alexandr-Andreevich/pet-project.git```

# Перейдите в директорию проекта
```cd pet-project```

2. Создайте и активируйте виртуальное окружение:
```bash
py -m venv .venv
.venv\Scripts\activate    # Windows
```

1. Установите зависимости:
```bash
py -m pip install -r requirements.txt
```

Перейдите в папку с проектом
```
cd app
```

3. Запустите миграции:
```bash
py manage.py migrate
```

4. Создайте суперпользователя:
```bash
py manage.py createsuperuser
```

5. Загрузите копии данных:
```bash
py manage.py loaddata fixtures/goods/categorii.json
py manage.py loaddata fixtures/goods/producti.json
```

6. Запустите сервер:
```bash
py manage.py runserver
```

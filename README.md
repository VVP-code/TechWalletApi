# WalletTK

Приложение для управления кошельками через REST API.  
Позволяет создавать кошельки, выполнять депозит, снимать средства и проверять баланс.

## Технологии

- Python 3.12  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- Docker + docker-compose  

## Установка и запуск

1. **Клонируйте репозиторий:**
```bash
git clone <URL_репозитория>
cd WalletTK
```

2. **Создайте файл `.env` в корне проекта и добавьте переменные:**
```env
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
POSTGRES_DB=wallet_db
POSTGRES_USER=wallet_user
POSTGRES_PASSWORD=wallet_pass
```

3. **Соберите и запустите Docker-контейнеры:**
```
docker-compose up --build -d
```

4. **Примените миграции:**
```
docker-compose run web python manage.py migrate
```

# Тесты 
```
docker-compose run web python manage.py test
```
Проверяется работа эндпоинтов DEPOSIT, WITHDRAW и контроль недостатка средств.
Тестовая база данных создаётся автоматически и уничтожается после тестов.
  
  ## Стиль кода

* Код соответствует стандарту PEP8.
* Миграции для базы данных присутствуют.
* Приложение устойчиво к конкурентным запросам (параллельные операции на одном кошельке корректно обрабатываются).

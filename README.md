# Книга рецептов

## Использование Docker

### Настройка проекта

Создайте `.env` файл в корне репозитория:

```bash
cp .env.dist .env
```

Внесите при необходимости корректировки в переменные окружения.

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Инициализация проекта

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec web bash
```

#### Применение миграций:

```bash
python manage.py migrate
```


#### Создание суперпользователя

```bash
python manage.py createsuperuser
```

Проект доступен по адресу http://127.0.0.1:8000

## Эндпоинты

### Регистрация

**URL** : `/api/register/`

**Method** : `POST`

**Auth required** : NO

**Data example**

```json
{
    "username": "example",
    "password": "lokum080",
    "password2": "lokum080",
    "email": "test@example.com"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "example",
    "email": "test@example.com"
}
```


### Получение токена

**URL** : `/api/token/`

**Method** : `POST`

**Auth required** : NO

**Data example**

```json
{
    "email": "test@example.com",
    "password": "lokum080"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDE0NDA1MCwiaWF0IjoxNjU0MDU3NjUwLCJqdGkiOiJiNDg1YzJlM2JmYTU0MTNkYmJhNzIzNjc5ZGQzNWVkNCIsInVzZXJfaWQiOjF9.SRcdkT4DchIplOYB4JLaVoliElOfiL1XCPWJkabJVYc",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MDU4MjUwLCJpYXQiOjE2NTQwNTc2NTAsImp0aSI6IjM2NTU4MDEwN2U3NjQyYmFhNGMxOTE0MWJlODRjYmU0IiwidXNlcl9pZCI6MX0.iFTJpzNpE5TBer9vcA7fRQeXyDQznprGlYofL6EKGag"
}
```

### Обновление токена

**URL** : `/api/token/refresh/`

**Method** : `POST`

**Auth required** : NO

**Data example**

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDE0NDA1MCwiaWF0IjoxNjU0MDU3NjUwLCJqdGkiOiJiNDg1YzJlM2JmYTU0MTNkYmJhNzIzNjc5ZGQzNWVkNCIsInVzZXJfaWQiOjF9.SRcdkT4DchIplOYB4JLaVoliElOfiL1XCPWJkabJVYc"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MDU4MzY5LCJpYXQiOjE2NTQwNTc2NTAsImp0aSI6IjYyNjU2ZGQyYzFlOTQ0N2M5YmIwZjdkZGI4MmNiYzg4IiwidXNlcl9pZCI6MX0.uVHAhQgdbl6X0sZyJT7BoolEk1Z7Vkrxnu6n50x_y78"
}
```

### Проверка токена

**URL** : `/api/token/verify`

**Method** : `POST`

**Auth required** : NO

**Data example**

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MDU4MzY5LCJpYXQiOjE2NTQwNTc2NTAsImp0aSI6IjYyNjU2ZGQyYzFlOTQ0N2M5YmIwZjdkZGI4MmNiYzg4IiwidXNlcl9pZCI6MX0.uVHAhQgdbl6X0sZyJT7BoolEk1Z7Vkrxnu6n50x_y78"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{}
```

### Logout

**URL** : `/api/logout/`

**Method** : `POST`

**Auth required** : YES

**Data example**

```
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MDU4MzY5LCJpYXQiOjE2NTQwNTc2NTAsImp0aSI6IjYyNjU2ZGQyYzFlOTQ0N2M5YmIwZjdkZGI4MmNiYzg4IiwidXNlcl9pZCI6MX0.uVHAhQgdbl6X0sZyJT7BoolEk1Z7Vkrxnu6n50x_y78'
```

### Success Response

**Code** : `401 Unauthorized`

**Content example**

```json
{"detail":"Данный токен недействителен для любого типа токена","code":"token_not_valid","messages":[{"token_class":"AccessToken","token_type":"access","message":"Токен недействителен или просрочен"}]}
```

### Добавление поста

**URL** : `/api/posts/`

**Method** : `POST`

**Auth required** : YES

**Data example**

```json
{
    "title": "Заголовок",
    "body": "Текст"
}
```

### Success Response

**Code** : `201 Created`

**Content example**

```json
{ 
  "id":1,
  "author":1,
  "author_username":"example",
  "title":"Заголовок",
  "body":"Текст",
  "like":0,
  "created_at":"2022-06-01T07:49:21.415645+03:00",
  "updated_at":"2022-06-01T07:49:21.415694+03:00"
}
```

### Вывод всех постов

**URL** : `/api/posts/`

**Method** : `GET`

**Auth required** : YES

**Data example**

```json
{}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
[
  {
    "id":1,
    "author":1,
    "author_username":"example",
    "title":"Заголовок",
    "body":"Текст",
    "like":0,
    "created_at":"2022-06-01T07:49:21.415645+03:00",
    "updated_at":"2022-06-01T07:49:21.415694+03:00"
  }
]
```

### Вывод определенного поста

**URL** : `/api/posts/<pk>`

**Method** : `GET`

**Auth required** : YES

**Data example**

```json
{}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "id":1,
    "author":1,
    "author_username":"example",
    "title":"Заголовок",
    "body":"Текст",
    "like":0,
    "created_at":"2022-06-01T07:49:21.415645+03:00",
    "updated_at":"2022-06-01T07:49:21.415694+03:00"
  }
```

### Лайкнуть пост

**URL** : `/api/posts/<pk>/like/`

**Method** : `GET`

**Auth required** : YES

**Data example**

```json
{}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{"detail":"Вы поставили лайк"}
```

### Убрать лайк

**URL** : `/api/posts/<pk>/unlike/`

**Method** : `GET`

**Auth required** : YES

**Data example**

```json
{}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{"detail":"Вы убрали лайк"}
```

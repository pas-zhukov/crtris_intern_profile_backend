# Личный кабинет стажёра. Бэкенд

## Как развернуть при помощи Docker

Сборка образа:
```bash
sudo docker build -t profile_backend .
```

Запуск контейнера:

```bash
sudo docker run -d profile_backend
```

## Развернуть без контейнера

Необходим Python 3.10 (можно и старше, но последние версии не рекомендуются, т.к. нестабильны)

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить

```bash
python manage.py runserver 0.0.0.0:8000
```
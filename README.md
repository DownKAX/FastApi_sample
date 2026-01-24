---

# FastApi_sample/auth_ready

Шаблон для приложения на **FastAPI** с аутентификацией, PostgreSQL, Alembic-миграциями, Redis, Docker и базовой архитектурой для реального API.

---
# FastApi_sample/blank

Шаблон с минимально реализованными структурами проекта для чистого старта - settings.py(у кого то config.py); UnitOfWork и Repositories, Service для него, logger, alembic, redis.
Готовая структура с минимальными набросками - конечные точки; тесты; модели базы данных; прочие модели для конечных точек, репозиториев.


---

# FastApi_sample/cheat_sheet
Небольшая ветка с реализованным функционалом конечных точек, служит чисто как напоминалка базовых вещей.

---

## Обзор auth_ready

Этот репозиторий - пример базового backend-проекта на Python + FastAPI, предназначенный для старта разработки API «с нуля». Включает:

* FastAPI + Uvicorn для сервера HTTP;
* Аутентификацию (JWT / OAuth2 Bearer);
* SQL-слой через SQLAlchemy;
* Миграции базы данных через Alembic;
* PostgreSQL как основная база;
* Redis-клиент;
* Docker-окружение;
* Unit-тесты.

## Основные возможности

*  **Аутентификация** (JWT/OAuth2) с refresh токенами, device id
*  **PostgreSQL + SQLAlchemy** для работы с данными
*  **Alembic** для миграций схемы БД
*  **Docker & Docker Compose**
*  **Redis-клиент** для кеша / сессий / брокера
*  **Unit тесты** (pytest)
*  **Готовая структура проекта** — папки `app/`, `tests/`, конфиги

---

##  Технологии и библиотеки

Зависимости, которые чаще всего используются в этом шаблоне:

* **SQLAlchemy** – ORM для работы с PostgreSQL
* **Alembic** – миграции схемы БД
* **psycopg2** / **asyncpg** – драйвер PostgreSQL
* **python-jose** / **passlib** – JWT и хэширование паролей
* **OAuth2 Password (Bearer)** – схема безопасности
* **redis** / **aioredis** – клиент для Redis
* **pytest** – тестирование
* **docker / docker-compose** – контейнеризация

---

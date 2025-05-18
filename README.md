# FastAPI, SQLALCHEMY, ONION ARCHITECTURE, JWT
 * Данное приложение совмещает в себе fastapi, sqlalchemy, 
postgresql и представляет собой базу для быстрого развертывания приложения с необходимым функционалом.
 * Приложение построено на onion architecture, тут есть слои repository, schemas, services, routing.
 * Также разработана система авторизации пользователя.

# Launch
* необходимо создать файл ".env" следующие переменные:

  - APP_PORT # порт, на котором будет запускаться приложение
  - REDIS_PASSWORD
  - REDIS_USER
  - REDIS_USER_PASSWORD
  - REDIS_HOST
  - REDIS_PORT


* Выполнить команду:
    
    docker compose up --build

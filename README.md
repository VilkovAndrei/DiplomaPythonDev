# Library API

## Проект "REST API для управления библиотекой"  
Данный проект представляет собой бэкенд-часть SPA веб-приложения
для для управления библиотекой.  
API предоставляет возможности для управления книгами, авторами
и пользователями, а также для отслеживания выдачи книг пользователям.   
Для реализации API использовался Django Rest Framework (DRF).

### Технологии
Python  
Django (Django REST framework, Celery)  
JWT и Permissions
PostgresQL (БД для хранения данных)  
Docker и Docker Compose

### Функциональные возможности
Регистрация и авторизация пользователей, получение информации о пользователях.  
Создание, редактирование и удаление авторов. Получение списка всех авторов.   
Создание, редактирование и удаление жанров. Получение списка всех жанров.  
Создание, редактирование и удаление книг. Получение списка всех книг. 
Поиск книг по различным критериям (название, автор, жанр, язык).   
Создание, редактирование и удаление экземпляров книг.
Получение списка всех экземпляров книг.   
Создание, редактирование и удаление информации о выдаче книги пользователю.
Получение списка выданных экземпляров книг. Отслеживание и редактирование
статуса возврата книги.   
Отправка напоминаний о наступлении срока возврата книги на email пользователя.

### Запуск проекта из Docker:
Склонируйте репозиторий git@github.com:VilkovAndrei/DiplomaPythonDev.git   
Создайте файл .env. Введите туда свои настройки как указано в файле .env.sample_docker
Установите Docker.   
В консоли запустите команду docker-compose up -d --build   
Пользователь для доступа в админ-панель Django: admin@test.com - "1234"

### Запуск проекта на Windows:
Склонируйте репозиторий https://github.com/VilkovAndrei/DiplomaPythonDev  
Создайте виртуальное окружение python -m venv venv  
Активируйте виртуальное окружение venv\Scripts\activate  
Установите зависимости проекта, указанные в файле requirements.txt:  
pip install -r requirements.txt  
Создайте файл .env. Введите туда свои настройки как указано в файле .env.sample_local  
Установите redis локально себе на компьютер  
После установки запустите сервер Redis в терминале с помощью:  
redis-server  
в терминале запускайте сервис:  
python manage.py runserver  
Запустите Celery для обработки отложенных задач:  
celery -A config worker -l INFO -P eventlet  
celery -A config beat -l info  

### Фикстуры и сервисные функции
Загрузить данные  из файла фикстур data.json в базу можно командой:   
python manage.py loaddata -Xutf8 data.json  
Пользователи из фикстур:  
admin@test.com  
user1@test.com  
manager@test.com  - менеджер (назначена группа 'manager'), основной пользователь для работы с API.   
пароли у всех по умолчанию - "1234"

Создать суперюзера можно командой:  
python manage.py csu  
создается пользователь (superuser):  
admin@test.com - "1234"
### Логирование
Результат работы сервиса по отправке напоминаний на email можно посмотреть
в лог-файле logs/mailing.log


### Документация API
Документация API доступна после запуска сервера по адресу:  
http://localhost:8000/redoc/    
или http://localhost:8000/docs/

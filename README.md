
# Boomerang Test

Инструкция по развертыванию и запуску Backend приложения

1) Склонируйте данный репозиторий с помощью команды:

```
$ git clone https://github.com/312NoMad/TestCookBook.git
```

2) Создать файл .env и заполнить его, используя для примера файл env_example


3) Для того чтобы приступить к следующему шагу у вас обязательно должен быть скачан Docker и Docker Compose. Если нет то вот ссылка на [документацию](https://docs.docker.com/desktop/?_gl=1*1fv4xo0*_ga*NjkxNTI0OTQzLjE2ODg3MTgxMTY.*_ga_XJWPQMJYHQ*MTcwNjQ3MTIwNy4zLjEuMTcwNjQ3MTIyMi40NS4wLjA.)

4) Запускаем наши контейнеры
```
$ docker-compose up --build
```

5) Если docker-compose удачно запустился и можно открыть страницу по URL адресу http://localhost:8000 , то останавливаем всё комбинацией клавиш Ctrl+C. Запускаем снова но уже командой:
```
$ docker-compose up -d --build
```

6) После успешного запуска применяем создаем и применяем миграции командами:
```
$ docker-compose exec web python manage.py makemigrations
$ docker-comopse exec web python manage.py migrate
```

7) Создаем суперюзера
```
$ docker-compose exec web python manage.py createsuperuser
```

Приложение готово к работе! Теперь можно смотреть и тестировать проект.



Адрес админ панели: http://localhost:8000/admin/

Адрес документации: http://localhost:8000/swagger/


8) Для запуска unit тестов используем команду:
```
$ docker-compose exec web python manage.py test
```
# ZOO HOSTEL

Веб-приложение для управления базой данных животных. 
База данных:  PostgreSQL.
Перед использованием, необходимо создать базу в PostgreSQLL
```
База: django_db
Имя пользователя: django_db
Пароль: django_pass
Адрес: 127.0.0.1:5427
```

Адреса приложения:
```
yourserver/ - список всех животных, Веб-версия
yourserver/<id животного>/undelete/ - восстановление удаленного животного
yourserver/api - API, список всех животных в формате Кличка, Приметы 
yourserver/detail/<id животного>/ - API, просмотр/редактирование/удаление животного
yourserver/animals/detail/ -  API, добавление животных
```

Некоторые особенности:
1. для доступа по API поддерживается Basic Auth
2. Каждый авторизованный пользователь может видеть животных только из своего приюта (Пользователь и есть приют)
3. Перемещать животных между приютами может только суперпользователь
4. Удалять животных может только суперпользователь. Используется soft delete.
   Восстановить можно по адресу yourserver/<id животного>/undelete/
5. Животное не может быть добавлено будущим днем
6. Вес животного от 1 грамма до 100 кг, рост животного до 99кг, возвраст до 99 лет
7. Картинки котиков подгружаются рандомно из интернета)

Установка:
```
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py loaddata dumpdata.json
  python manage.py runserver
```
Доступны пользователи:

Superuser, login:django_admin pass:django_pass

User(Staff), login:South pass:justpass

 

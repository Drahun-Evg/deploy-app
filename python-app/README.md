## Документация


> #### Запуск проект
1. docker-compose build
2. docker-compose up

> #### Полезные команды:
* sudo chown -R $USER /home/user/PycharmProjects/support/data

> #### Адреса:

1. /api/v1/ticket/
> * создать тикет
> * отображаются все тикеты
2. /api/v1/message/
> * написать сообщение к тикету
3. /api/v1/ticket/<int:pk>
> * <int:pk> - id тикета
> * отображаеться тикет с сообщениями
> * удалить тикет
4. /api/v1/ticket/update/<int:pk>
> * <int:pk> - id тикета
> * изменить статус тикета
5. /api/token/
> * получить токены
6. api/token/refresh/
> * обновить токен
7. api/token/verify/
> * верификация по токену

Для проверки работы celery необходимо прописать email и пароль от почты в settings.py

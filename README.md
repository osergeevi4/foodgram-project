[![foodgram](https://github.com/osergeevi4/foodgram-project/actions/workflows/foodgram_workflow.yaml/badge.svg)](https://github.com/osergeevi4/foodgram-project/actions/workflows/foodgram_workflow.yaml)
# Foodgram
​
Выпускной проект в рамках Яндекс.Практикума.
Foodgram - сервис для размещения своих рецептов.
На сайте можно добавить свой рецепт, подписаться на интересного Вам автора, добавить чужой рецепт в 'Избранное' и в конечном итоге скачать список покупок.
Посмотреть в живую можно здесь: http://130.193.44.6/
​
## Требования
​
Перед запуском работы проверьте наличие 
[Python](https://www.python.org/downloads/),
[Django](https://www.djangoproject.com/), 
[Docker](https://www.docker.com/).
​
## Установка
​
*Клонируйте репозиторий на локальный компьютер. 
Выполните сборку контейнера.*
```
$ docker-compose build
```
​
*Запуск docker-compose.*
```
$ docker-compose up
```
При создании контейнера миграции выполнятся автоматически.
​
## Первоначальная загрузка ингредиентов и тэгов.
```
$ docker-compose run <CONTAINER ID> python manage.py load_ingredients_tags
```
​
## Создание суперпользователя.
```
$ docker-compose run <CONTAINER ID> python manage.py createsuperuser
```
## Выключение контейнеров.
```
docker-compose down
```
## Удаление контейнеров.
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

# Домашнее задание №11

## Кобана Давида


### Google Sheet table


https://docs.google.com/spreadsheets/d/10J-A-B-RAYCQgm4ZOqUnOGVo-PBY29vZrOUI1DvULL0/edit?pli=1#gid=0


### Telegram bot

https://t.me/deliverytimeendbot


## Инструкци запуска

Для запуска контейнеров Docker советую установить Docker Desktop

```
git clone https://github.com/DavidKoban/Hillel_Homework/

cd Hillel_Homework

docker-compose build

docker-compose up -d

docker-compose exec app python manage.py makemigrations test_task

docker-compose exec app python manage.py migrate

docker-compose restart
```

После чего перейдите по ссылке 

http://127.0.0.1:8000/

или

http://localhost:8000/

## Объяснение кода

Каждую минуту обновляется база данных и html-страница

Каждый день в 10:00 обновляется курс доллара и отсылается сообщение телеграм ботом 

об окончании поставки какого-то заказа

Для последнего задания было предложено добавить поле, которое показывает было ли отправлено сообщение 

по поводу заказа или нет в модель Order, но т.к. сообщение отправляется 1 раз в день я могу гарантировать что заказы 

у которых срок поставки закончился вчера не будут продублированны сегодня  

.env файл был добавлен СПЕЦИАЛЬНО для удобности

# Домашнее задание №11

## Кобана Давида


### Google Sheet table


https://docs.google.com/spreadsheets/d/10J-A-B-RAYCQgm4ZOqUnOGVo-PBY29vZrOUI1DvULL0/edit?pli=1#gid=0


### Telegram bot

https://t.me/deliverytimeendbot


## Инструкци запуска

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


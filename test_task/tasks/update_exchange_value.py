import requests
from test_task.models import Config
from core.celery import app


@app.task
def update_exchange_value():
    url = 'https://api.monobank.ua/bank/currency'
    curses = requests.get(url).json()
    for curs in curses:
        if curs['currencyCodeA'] == 840 and curs['currencyCodeB'] == 980:
            try:
                Config.objects.first.update(exchange_value=curs['rateBuy'])
            except:
                Config.objects.create(exchange_value=curs['rateBuy'])
            break

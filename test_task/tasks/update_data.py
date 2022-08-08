import decimal
from datetime import datetime
from test_task.functions.get_table_values.get_table_values import get_table_values
from test_task.models import Order, Config
from core.celery import app
from test_task.tasks.update_exchange_value import update_exchange_value


@app.task
def update_data():
    table_values = get_table_values()
    processed_ids = []
    exchange_value = Config.objects.first()
    if exchange_value is None:
        update_exchange_value()
        exchange_value = Config.objects.first()
    exchange_value = exchange_value.exchange_value
    for line in table_values:
        try:
            order, updated = Order.objects.update_or_create(
                table_id=line['table_id'],
                defaults={
                    'order_number': line['order_number'],
                    'cost_usd': line['cost_usd'],
                    'cost_uah': (line['cost_usd']*exchange_value).quantize(decimal.Decimal(1.00), decimal.ROUND_05UP),
                    'delivery_time': datetime.strptime(line['delivery_time'], '%d.%m.%Y'),
                },
            )
            processed_ids.append(line['table_id'])
        except:
            pass
    Order.objects.exclude(table_id__in=processed_ids).delete()


from django.utils import timezone
from core.celery import app
from test_task.models import User
from test_task.models import Order
from bot import bot


@app.task
def sent_telegram_messege_on_10_am():
    orders_list_delivery_time_end = Order.objects.filter(delivery_time=timezone.now().date()).values_list('order_number')
    users_list_id = User.objects.values_list('telegram_id')
    if orders_list_delivery_time_end == []:
        for user_id in users_list_id:
            bot.send_message(user_id[0],
                         "Привет, сегодня нет заказов у которых закнчивается срок поставки")

    else:
        str_orders_list_delivery_time_end = 'Привет, сегодня заканчивается срок поставки\n'
        for order_delivery_time_end in orders_list_delivery_time_end:
            str_orders_list_delivery_time_end = str_orders_list_delivery_time_end + str(order_delivery_time_end[0]) + "\n"
        for user_id in users_list_id:
            bot.send_message(user_id[0], str_orders_list_delivery_time_end)

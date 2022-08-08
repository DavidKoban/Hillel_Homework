from django.db import models


# Модель заказа
class Order(models.Model):
    table_id = models.IntegerField(default=0, null=False)
    order_number = models.IntegerField(default=0, null=False, unique=True)
    cost_usd = models.DecimalField(default=0, null=False, max_digits=10, decimal_places=2)
    cost_uah = models.DecimalField(default=0, null=False, max_digits=10, decimal_places=2)
    delivery_time = models.DateField(null=False)

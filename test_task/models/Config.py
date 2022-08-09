from django.db import models


#Модель для хранения курса
class Config(models.Model):
    exchange_value = models.DecimalField(null=False, max_digits=10, decimal_places=2)

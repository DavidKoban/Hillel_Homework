from django.db import models


#Модель для хранения id чатов для отсыслки сообщений
class User(models.Model):
    telegram_id = models.IntegerField(default=000000000, null=False)

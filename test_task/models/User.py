from django.db import models


class User(models.Model):
    telegram_id = models.IntegerField(default=000000000, null=False)

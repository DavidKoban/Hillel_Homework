import os
import telebot
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from test_task.models import User


bot = telebot.TeleBot('5344051604:AAHl0HVkNG6UEX0h0DYR7nqnwPTSnKanzwI')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    User.objects.create(telegram_id=m.chat.id)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)


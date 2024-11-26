import telebot

bot = telebot.TeleBot('7570166868:AAGBCdlys2bmncR7hG07418qK6tLyyEBMJs')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Теперь ты можешь быстро найти самые важные ссылки и материалы!')


@bot.message_handler(commands=['vavt'])
def site(message):
    bot.send_message(message.chat.id, 'Лови ссылку на сайт универа: https://www.vavt.ru')


@bot.message_handler(commands=['ege'])
def mathew(message):
    bot.send_message(message.chat.id, 'Вот ссылка на самый нужный сайт в этом деле: https://ege.sdamgia.ru')


@bot.message_handler(commands=['schedule'])
def goog(message):
    bot.send_message(message.chat.id, 'Твое личное расписание и список дел здесь: https://calendar.google.com/')


bot.infinity_polling()
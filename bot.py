from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime
import re

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = 'Привет, {}! Ты написал: {}'.format(
        update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s',
                 update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def word_count(bot, update):
    input = re.split(r'[ ,]+', update.message.text)
    if len(input) > 1:
        result = len(input)-1
        update.message.reply_text(f'Слов: {result}')
    else:
        update.message.reply_text('Некорректный ввод')


def next_full_moon(bot, update):
    input = update.message.text.split()
    try:
        date = input[1]
        datetime.datetime.strptime(date, '%Y-%m-%d')
        result = ephem.next_full_moon(date)
        text = 'Ближайшее полнолуние {}.'.format(result)
        update.message.reply_text(text)
    except (ValueError, IndexError):
        text = 'Команда принимает дату в формате YYYY-MM-DD'
        update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("wordcount",  word_count))
    dp.add_handler(CommandHandler("next_full_moon",  next_full_moon))

    mybot.start_polling()
    mybot.idle()


main()

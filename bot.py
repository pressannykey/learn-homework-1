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
    text = 'Приветствую!'
    update.message.reply_text(text)

    logging.info('User: %s, Message: %s',
                 update.message.chat.username, text)


def talk_to_me(bot, update):
    text = '{}, ты написал: {}'.format(
        update.message.chat.first_name, update.message.text)
    update.message.reply_text(text)

    logging.info('User: %s, Message: %s --> Answer: %s',
                 update.message.chat.username, update.message.text, text)


def word_count(bot, update):
    input = re.split(r'[ ,]+', update.message.text)
    if len(input) > 1:
        result = len(input)-1
        text = f'Слов: {result}'
        update.message.reply_text(text)
    else:
        text = 'Напиши что-нибудь после /wordcount, а я посчитаю количество слов'
        update.message.reply_text(text)

    logging.info('User: %s, Message: %s --> Answer: %s',
                 update.message.chat.username, update.message.text, text)


def next_full_moon(bot, update):
    input = update.message.text.split()
    try:
        date = input[1]
        datetime.datetime.strptime(date, '%Y-%m-%d')
        result = ephem.next_full_moon(date)
        text = 'Ближайшее полнолуние {}.'.format(result)
        update.message.reply_text(text)
    except (ValueError, IndexError):
        text = 'Напиши после /next_full_moon дату в формате YYYY-MM-DD, а я расскажу, когда ближайшее полнолуние'
        update.message.reply_text(text)

    logging.info('User: %s, Message: %s --> Answer: %s',
                 update.message.chat.username, update.message.text, text)


def get_constellation(bot, update):
    user_input = update.message.text.split()
    if len(user_input) > 1:
        planet = user_input[1].capitalize()
        today = update.message.date
        try:
            result = ephem.constellation(getattr(ephem, planet)(today))
            text = 'Cегодня {} в созвездии {}!'.format(planet, result[1])
            update.message.reply_text(text)
        except AttributeError:
            text = 'Такой планеты не существует'
            update.message.reply_text(text)
    else:
        text = 'Напиши после /planet название планеты на английском, а я расскажу, в каком она созвездии сегодня'
        update.message.reply_text(text)

    logging.info('User: %s, Message: %s --> Answer: %s',
                 update.message.chat.username, update.message.text, text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("wordcount",  word_count))
    dp.add_handler(CommandHandler("next_full_moon",  next_full_moon))
    dp.add_handler(CommandHandler("planet", get_constellation))

    mybot.start_polling()
    mybot.idle()


main()

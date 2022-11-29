"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log', encoding='utf-8')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet(update, context):
    planet_name = update.message.reply_text.split()[1].capitalize()
    planet = ephem.Mars(datetime.now())
    if hasattr(planet_name, ephem):
       planet = getattr(planet_name, ephem)
       print(ephem.constelation(planet()))
    


def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(text)


def main():
    mybot = Updater("5981325352:AAH6iOrcQs7iug7emxDnxYxdDprbawHeDGw", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стратовал!')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

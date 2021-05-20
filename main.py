from telebot.types import ReplyKeyboardMarkup, Update
from functions import *
from config import *
from Csv import *
import telebot
import datetime
import threading 
import os


bot = telebot.TeleBot(TOKEN)

threading.Thread(target=timer).start() # запуск в фоне цункции проверки


# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, startMessage)
    addUtilizer(str(message.from_user.id))
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['schedule'])
def sendingSchedule(message):

    jsonToCsv(str(message.chat.id))
    BuildingAGraphFromCsv()

    image = open('line_plot.png', 'rb')

    bot.send_photo(message.chat.id, image)

    os.remove('line_plot.png')
    
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['teststart'])
def testStart(message):
    timeToTearAndThrow()
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(content_types=['text'])
def processingTextResponses(message):
    # message.text

    now = datetime.datetime.now()
    time = str(now.hour) + ':00'

    addData(str(message.chat.id), time, message.text)

    bot.send_message(message.chat.id, 'Ваш ответ записан', reply_markup = None)
# --------------------------------------------------------------------------------------------------------



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)

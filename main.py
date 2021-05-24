from telebot.apihelper import send_message
from functions import *
from config import *
from Csv import *
import telebot
import datetime
import threading 
import os


bot = telebot.TeleBot(TOKEN)

threading.Thread(target = timer).start() # запуск в фоне функции проверки


# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, startMessage)
    addUtilizer(str(message.from_user.id))
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['schedule'])
def sendingSchedule(message):
    pngName = jsonToCsv(str(message.chat.id))
    image = open(pngName, 'rb')
    bot.send_photo(message.chat.id, image)
    os.remove(pngName)
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['teststart'])
def testStart(message):
    timeToTearAndThrow()
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['NumberOfUsers'])
def numberOfUsers(message):
    data = jsonReader()

    if message.chat.id == 538024314:
        bot.send_message(message.chat.id, len(data))
    else:
        bot.send_message(message.chat.id, 'Вы не можете получать эти данные!')
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(content_types=['text'])
def processingTextResponses(message):
    # message.text

    now = datetime.datetime.now()
    # time = str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute)
    time = '{0}-{1} {2}:{3}'.format(now.month, now.day, now.hour, beaMin(now.minute))

    addData(str(message.chat.id), time, message.text)

    bot.send_message(message.chat.id, 'Ваш ответ записан')
# --------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['stop'])
def stop(message):
    if removeUtilizer(message.chat.id):
        message.send_message(message.chat.id, successfulDeletion)
    else:
        message.send_message(message.chat.id, unsuccessfulDeletion)
# --------------------------------------------------------------------------------------------------------



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)

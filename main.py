from functions import *
from config import *
from Csv import *
import telebot
import datetime
import threading 
import os


bot = telebot.TeleBot(TOKEN)

threading.Thread(target = timer).start() # запуск в фоне функции проверки


# --------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, startMessage)
    addUtilizer(str(message.from_user.id))
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

@bot.message_handler(commands=['schedule'])
def sendingSchedule(message):
    pngName = jsonToCsv(str(message.chat.id), message.from_user.first_name)
    image = open(pngName, 'rb')
    bot.send_photo(message.chat.id, image)
    os.remove(pngName)
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

@bot.message_handler(commands=['stop'])
def stop(message):
    if removeUtilizer(message.chat.id):
        bot.send_message(message.chat.id, successfulDeletion)
    else:
        bot.send_message(message.chat.id, unsuccessfulDeletion)
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
@bot.message_handler(commands=['teststart'])
def testStart(message):
    bot.send_message(message.chat.id, offTestStart)
    #timeToTearAndThrow()
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
@bot.message_handler(commands=['what_is_my_id'])
def what_is_my_id(message):
    bot.send_message(message.chat.id, message.chat.id)
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
@bot.message_handler(commands=['NumberOfUsers'])
def numberOfUsers(message):
    data = jsonReader()

    if message.chat.id == 538024314:
        bot.send_message(message.chat.id, len(data))
    else:
        bot.send_message(message.chat.id, 'Вы не можете получать эти данные!')
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def processingTextResponses(message):
    # message.text

    now = datetime.datetime.now()
    # time = str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute)
    time = '{0}-{1} {2}:{3}'.format(now.month, 
                                    now.day, 
                                    now.hour, 
                                    beaMin(now.minute))

    try:
        addData(str(message.chat.id), time, int(message.text))
    except Exception as e:
        print(e)

    bot.send_message(message.chat.id, 'Ваш ответ записан')
# --------------------------------------------------------------------------------



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)

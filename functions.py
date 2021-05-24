import json
import time
import datetime
import telebot
from config import *
from telebot import types


bot = telebot.TeleBot(TOKEN)

# --------------------------------------------------------------------------------------------------------

# Запись в файл
def jsonWriter(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

# --------------------------------------------------------------------------------------------------------

# Чтение файла
def jsonReader():
    with open('data.json') as inputFile:
        data = json.load(inputFile)

    return data

# --------------------------------------------------------------------------------------------------------

# Добавление пользователя
def addUtilizer(name):
    data = jsonReader()

    try:
        data[name]
    except:
        data[name] = []

        jsonWriter(data)

# --------------------------------------------------------------------------------------------------------

# Проверка на наличие пользоватиля
def utilizerCheck(data, name):
    try:
        data[name]
        return True

    except:
        return False

# --------------------------------------------------------------------------------------------------------

# Добовление данных 
def addData(name, time, appraisal):

    data = jsonReader()
    time = '\"' + time + '\"'

    utilizer = data[name]
    newData = [time, appraisal]


    if len(utilizer) > 0:
        if utilizerCheck(data, name) and utilizer[-1][0] != newData[0]:
        
            utilizer.append(newData)
            jsonWriter(data)

    else:

        utilizer.append(newData)
        jsonWriter(data)

# --------------------------------------------------------------------------------------------------------

def askaQuestion(chatId): 
    now = datetime.datetime.now()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')


    bot.send_message(
    chatId,
    'Your rating at {0}:{1} : '.format(now.hour, beaMin(now.minute)),
    reply_markup = markup,)

# --------------------------------------------------------------------------------------------------------

# Вопрос для пользователя 
def timeToTearAndThrow():
    data = jsonReader()

    for chatId in data:
        askaQuestion(chatId)

# --------------------------------------------------------------------------------------------------------

# Если ровно час (9:00, 12:00...22:00), то активирует функцию "опроса" (timeToTearAndThrow)
def timer():
    while True:
        now = datetime.datetime.now()

        # Да, Капэць
        # Если минута = 0 и часы не равны 1-9
        if now.hour != 1 or 2 or 3 or 4 or 5 or 7 or 8 or 9:
            if now.minute == 0: 
                print(now.minute)
                timeToTearAndThrow()
                time.sleep(3480)
        
        time.sleep(5)
            
# --------------------------------------------------------------------------------------------------------

# beautiful Minutes
beaMin = lambda minute : '0' + str(minute) if minute < 10 else minute 

# --------------------------------------------------------------------------------------------------------

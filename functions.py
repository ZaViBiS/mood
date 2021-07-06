import json
import time
import datetime

import telebot

from config import *
from telebot import types


bot = telebot.TeleBot(TOKEN)

# --------------------------------------------------------------------------------


def jsonWriter(data): # Запись в файл
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

# --------------------------------------------------------------------------------

def jsonReader(): # Чтение файла
    with open('data.json') as inputFile:
        data = json.load(inputFile)

    return data

# --------------------------------------------------------------------------------

def addUtilizer(name): # Добавление пользователя
    data = jsonReader()

    try:
        data[name]
    except:
        data[name] = []

        jsonWriter(data)

# --------------------------------------------------------------------------------

def utilizerCheck(data, name): # Проверка на наличие пользоватиля
    try:
        data[name]
        return True

    except:
        return False

# --------------------------------------------------------------------------------

def addData(name, time, appraisal): # Добовление данных 

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

# --------------------------------------------------------------------------------

def askaQuestion(chatId): # Отправка вопроса
    now = datetime.datetime.now()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')


    bot.send_message(
    chatId,
    hourlyMessage + '{0}:{1} : '.format(now.hour, beaMin(now.minute)),
    reply_markup = markup)

# --------------------------------------------------------------------------------


def timeToTearAndThrow(): # Вопросы для пользователей 
    data = jsonReader()

    for chatId in data:
        askaQuestion(chatId)
# --------------------------------------------------------------------------------

def not_equal(hour):
    for x in range(10):
        if (x) == hour:
            return False
    return True
# --------------------------------------------------------------------------------

# Если ровно час (9:00, 12:00...22:00), то активирует функцию "опроса" (timeToTearAndThrow)
def timer():
    while True:
        now = datetime.datetime.now()
        # Если минута = 0 и часы не равны 0-9
        if not_equal(now.hour) and now.minute == 0:
            print(now.minute)
            timeToTearAndThrow()
            time.sleep(3480)
        
        time.sleep(5)
            
# --------------------------------------------------------------------------------

# beautiful Minutes
beaMin = lambda minute : '0' + str(minute) if minute < 10 else minute 

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

def removeUtilizer(utilizer): # Удаление пользователе и его данных
    utilizer = str(utilizer)
    data = jsonReader()

    try:
        del data[utilizer]
        jsonWriter(data)

        return True
    except:
        return False
# --------------------------------------------------------------------------------

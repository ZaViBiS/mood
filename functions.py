import json
import time
import datetime
import threading
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
    # kbGrades = Keyboa(items=listOfGrades, copy_text_to_callback=True).keyboard

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    buttonList = []


    for x in range(10):
        button = types.KeyboardButton(str(x + 1))
        buttonList.append(button)

 
    markup.add(
    buttonList[0], 
    buttonList[1],
    buttonList[2], 
    buttonList[3], 
    buttonList[4], 
    buttonList[5], 
    buttonList[6], 
    buttonList[7], 
    buttonList[8], 
    buttonList[9])
    


    bot.send_message(
    chatId,
    'Your rating at ' + str(now.hour) + ':00 : ',
    reply_markup = markup, 
    )

# --------------------------------------------------------------------------------------------------------

# Создание потоков для вопросов у пользователя 
def timeToTearAndThrow():
    data = jsonReader()

    for x in data:
        threading.Thread(target=askaQuestion, args=(x, )).start()

# --------------------------------------------------------------------------------------------------------

# Если ровно час (9:00, 12:00...22:00), то активирует функцию "опроса" (timeToTearAndThrow)
def timer():
    while True:
        now = datetime.datetime.now()

        # Да, Капэць
        # Если менута = 0 и часы не равны 1-9
        if now.minute < 1 and now.hour != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 : 
            timeToTearAndThrow()
            time.sleep(3480)
        
        time.sleep(5)
            
# --------------------------------------------------------------------------------------------------------

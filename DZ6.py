import psysuperbot 
from random import *
import json
import requests
tests = []
API_URL='https://7012.deeppavlov.ai/model'
def save():
    with open("tests.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(tests,ensure_ascii=False))
    print("Наши тесты были успешно сохранены в файле tests.json")
def load():
    global films
    with open("tests.json","r",encoding="utf-8") as fh:
        tests=json.load(fh)
    print("Тесты были успешно загружены")

API_TOKEN = "6737709947:AAHq13bzIkVAtTTb1D0aNobROD_CyNTrAlM"
bot = Si_BOT.PsysuperBot(API_TOKEN)

@bot.message_handler(commands=["start"])

def start_message(message):
    tests.append("Депрессия")
    tests.append(" Невроз")
    tests.append("Тревожность")
    tests.append("Зависимость")
    tests.append("Психические расстройства")
    bot.send_message(message.chat.id," Тесты были загружены по умолчанию")
@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id,"Вот список тестов")
    bot.send_message(message.chat.id, ", ".join(tests))

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1(inlove) 
    qq=" ".join(quest)
    data = { 'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")

bot.polling()

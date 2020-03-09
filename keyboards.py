# -*- coding:utf8 -*-

from telebot.types import ReplyKeyboardMarkup,KeyboardButton

def geo():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    button=KeyboardButton("Отправить координаты",request_location=True)
    kb.row(button)
    return kb

def weather():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    button1=KeyboardButton("Прогноз на сегодня")
    button2=KeyboardButton("Прогноз на завтра")
    button3=KeyboardButton("Прогноз на 5 дней")
    button4=KeyboardButton("Сменить координаты")
    kb.row(button1,button2)
    kb.row(button3)
    kb.row(button4)
    return kb
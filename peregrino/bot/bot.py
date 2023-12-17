import telebot

from peregrino.config import TOKEN
from peregrino.loggers import logger

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

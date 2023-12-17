import configparser
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
bot_conf_path = os.path.join(script_directory, '..', 'bot.conf')

config = configparser.ConfigParser()
config.read(bot_conf_path)

TOKEN = config['PEREGRINO']['TOKEN']
GROUP_LOG = int(config['PEREGRINO']['PEREGRINO_LOG'])
CHANNEL = int(config['PEREGRINO']['PEREGRINO_CHANNEL'])
BOT_NAME = config['PEREGRINO']['BOT_NAME']
BOT_USERNAME = config['PEREGRINO']['BOT_USERNAME']
OWNER = int(config['PEREGRINO']['OWNER_ID'])
CHANNEL_POST = int(config['PEREGRINO']['PEREGRINO_CHANNEL_POST'])
LOG_PATH = config['LOG']['LOG_PATH']
MONGO_CON = config['DB']['MONGO_CON']

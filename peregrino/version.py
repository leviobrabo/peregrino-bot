from sys import version_info

import telebot

python_version = f'{version_info[0]}.{version_info[1]}.{version_info[2]}'
peregrino_version = '0.1.0'
telebot_version = getattr(telebot, '__version__', 'Versão não encontrada')

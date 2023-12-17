from telebot import types

from bot import bot
from config import *
from database.db import *
from loggers import logger


def send_new_group_message(chat):
    try:
        chatusername = (
            f'@{chat.username}' if chat.username else 'Private Group'
        )
        bot.send_message(
            GROUP_LOG,
            text=f'#{BOT_USERNAME} #New_Group\n'
            f'<b>Chat:</b> {chat.title}\n'
            f'<b>ID:</b> <code>{chat.id}</code>\n'
            f'<b>Link:</b> {chatusername}',
            parse_mode='html',
            disable_web_page_preview=True,
        )
    except Exception as e:

        logger.error(f'Erro ao adicionador grupo no banco de dados: {e}')


@bot.my_chat_member_handler()
def send_group_greeting(message: types.ChatMemberUpdated):
    try:
        old_member = message.old_chat_member
        new_member = message.new_chat_member
        if message.chat.type != 'private' and new_member.status in [
            'member',
            'administrator',
        ]:
            chat_id = message.chat.id
            chat_name = message.chat.title

            if chat_id == CHANNEL:

                logger.warning(
                    f'Ignorando armazenamento de chat com ID {chat_id}, pois corresponde ao ID do canal configurado.'
                )

                return

            if chat_id == CHANNEL_POST:

                logger.warning(
                    f'Ignorando armazenamento de chat com ID {chat_id}, pois corresponde ao ID do canal configurado.'
                )

                return

            if chat_id == GROUP_LOG:

                logger.warning(
                    f'Ignorando armazenamento de chat com ID {chat_id}, pois corresponde ao ID do canal configurado.'
                )

                return

            existing_chat = search_group(chat_id)
            if existing_chat:

                logger.warning(
                    f'O bate-papo com ID {chat_id} já existe no banco de dados.'
                )

                return

            add_chat_db(chat_id, chat_name)

            logger.success(
                f'⭐️ O bot foi adicionado no grupo {chat_name} - ({chat_id})'
            )

            send_new_group_message(message.chat)

            if message.chat.type in ['group', 'supergroup', 'channel']:
                markup = types.InlineKeyboardMarkup()
                channel_ofc = types.InlineKeyboardButton(
                    'Canal Oficial 🇧🇷', url='https://t.me/peregrinosbr'
                )
                report_bugs = types.InlineKeyboardButton(
                    'Relatar bugs', url='https://t.me/kylorensbot'
                )
                markup.add(channel_ofc, report_bugs)
                bot.send_message(
                    chat_id,
                    'Olá, meu nome é Peregrino! Obrigado por me adicionar em seu grupo.\n\nSou um bot bíblicos, enviarei versículos bíblicos no grupo.\n\nEscolha o tema dos versículos /verstema',
                    reply_markup=markup,
                )
    except Exception as e:

        logger.error(f'Erro ao enviar mensagem de boas-vindas: {e}')


@bot.message_handler(content_types=['left_chat_member'])
def on_left_chat_member(message):
    try:
        if message.left_chat_member.id == bot.get_me().id:
            chat_id = message.chat.id
            chat_name = message.chat.title
            remove_chat_db(chat_id)
            logger.success(
                f'O bot foi removido do grupo {chat_name} - ({chat_id})'
            )
    except Exception as e:

        logger.error(f'Erro ao remover grupo do banco de dados: {e}')


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    try:
        chat_type = message.chat.type

        if chat_type in ['group', 'supergroup']:
            chat_id = message.chat.id
            chat_name = message.chat.title
            if chat_id == CHANNEL:
                return

            if chat_id == CHANNEL_POST:
                return

            if chat_id == GROUP_LOG:
                return

            existing_chat = search_group(chat_id)
            if existing_chat:
                return

            add_chat_db(chat_id, chat_name)

            logger.success(
                f'⭐️ O bot foi adicionado no grupo {chat_name} - ({chat_id})'
            )

            send_new_group_message(message.chat)

            if message.chat.type in ['group', 'supergroup', 'channel']:
                markup = types.InlineKeyboardMarkup()
                channel_ofc = types.InlineKeyboardButton(
                    'Canal Oficial 🇧🇷', url='https://t.me/peregrinosbr'
                )
                report_bugs = types.InlineKeyboardButton(
                    'Relatar bugs', url='https://t.me/kylorensbot'
                )
                markup.add(channel_ofc, report_bugs)
                bot.send_message(
                    chat_id,
                    'Olá, meu nome é Peregrino! Obrigado por me adicionar em seu grupo.\n\nSou um bot bíblicos, enviarei versículos bíblicos no grupo.\n\nEscolha o tema dos versículos /verstema',
                    reply_markup=markup,
                )
    except Exception as e:

        logger.error(f'Erro ao enviar mensagem de boas-vindas: {e}')

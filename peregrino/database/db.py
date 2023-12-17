from pymongo import ASCENDING, MongoClient

from peregrino import MONGO_CON, logger

try:

    logger.info('ℹ️ INICIANDO CONEXÃO COM O MONGODB')

    client = MongoClient(MONGO_CON)
    db = client.fatoshistbot
    logger.success('✅ Conexão com o MongoDB estabelecida com sucesso!')

except Exception as e:
    logger.error(f'❗️ Erro ao conectar ao MongoDB: {e}')

# Operações relacionadas a usuários


def add_user_db(message):
    first_name = message.from_user.first_name
    last_name = str(message.from_user.last_name).replace('None', '')
    username = str(message.from_user.username).replace('None', '')
    return db.users.insert_one(
        {
            'user_id': message.from_user.id,
            'firstname': first_name,
            'lastname': last_name,
            'username': username,
            'is_dev': 'false',
            'is_ban': 'false',
            'fowr_private': 'true',
            'diariavers': 'false',
            'versId': '',
            'blb365': 'false',
            'versiculoUser': '',
            'dia': '',
            'message': [],
            'messagePosition': '',
            'messageId': '',
            'motivosdeoracao': [],
            'blocodenotas': [],
            'horariodeoracao': '',
            'diasdeestudo': 0,
            'receivedPlusOne': 'false',
            'last_interaction': '',
            'translation': 'acf',
        }
    )


def get_all_users(query=None):
    if query:
        return db.users.find(query)
    else:
        return db.users.find({})


def search_user(user_id):
    return db.users.find_one({'user_id': user_id})


def remove_user_db(user_id):
    db.users.delete_one({'user_id': user_id})


def users_with_sudo():
    return db.users.find({'is_dev': 'true'})


def set_user_sudo(user_id):
    return db.users.update_one(
        {'user_id': user_id}, {'$set': {'is_dev': 'true'}}
    )


def un_set_user_sudo(user_id):
    return db.users.update_one(
        {'user_id': user_id}, {'$set': {'sudo': 'false'}}
    )

# Operações relacionadas aos chats


def add_chat_db(chat_id, chat_name):
    return db.chats.insert_one(
        {
            'chat_id': chat_id,
            'chat_name': chat_name,
            'blocked': 'false',
            'forwarding': 'true',
            'versdia': 'true',
            'verstema': 'Encorajamento',
            'last_interaction_group': ''
        }
    )


def get_all_chats(query=None):
    if query:
        return db.chats.find(query)
    else:
        return db.chats.find({})


def search_group(chat_id):
    return db.chats.find_one({'chat_id': chat_id})


def remove_chat_db(chat_id):
    db.chats.delete_one({'chat_id': chat_id})

# Operações relacionadas a planos


def add_plano_db(user_id, firstname):
    return db.plano.insert_one(
        {
            'user_id': user_id,
            'firstname': firstname,
            'planoAtivo': 'false',
            'diaPlano': '',
            'versiculoPlano': '',
            'messagePlano': [],
            'messagePositionPlano': '',
            'messageIdPlano': '',
            'planosConcluidos': 0,
            'plano1': 'false',
            'plano2': 'false',
            'plano3': 'false',
            'plano4': 'false',
            'plano5': 'false',
            'plano6': 'false',
            'plano7': 'false',
            'plano8': 'false',
            'plano9': 'false',
            'plano10': 'false',
            'plano11': 'false',
            'plano12': 'false',
            'plano13': 'false',
            'plano14': 'false',
            'plano15': 'false',
            'plano16': 'false',
            'plano17': 'false',
            'plano18': 'false',
            'plano19': 'false',
            'plano20': 'false',
            'plano21': 'false',
            'plano22': 'false',
            'plano23': 'false',
            'plano24': 'false',
            'plano25': 'false',
            'plano26': 'false',
            'plano27': 'false',
            'plano28': 'false',
            'plano29': 'false',
            'plano30': 'false'
        }
    )

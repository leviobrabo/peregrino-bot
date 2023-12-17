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


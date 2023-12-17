from pymongo import ASCENDING, MongoClient

from peregrino import MONGO_CON
from peregrino import logger

try:

    logger.info('ℹ️ INICIANDO CONEXÃO COM O MONGODB')

    client = MongoClient(MONGO_CON)
    db = client.fatoshistbot
    logger.success('✅ Conexão com o MongoDB estabelecida com sucesso!')

except Exception as e:
    logger.error(f'❗️ Erro ao conectar ao MongoDB: {e}')

# Operações relacionadas a usuários

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
ADMINS_CHAT = env.str("ADMINS_CHAT")
IP = env.str("ip")


HOST_DB = env.str('HOST_DB')
USER_DB = env.str('USER_DB')
PASSWORD_DB = env.str('PASSWORD_DB')
DATABASE_DB = env.str('DATABASE_DB')


WEBHOOK_HOST = env.str('WEBHOOK_HOST')
WEBHOOK_PATH = env.str('WEBHOOK_PATH')

WEBHOOK_SSL_CERT = env.str('WEBHOOK_SSL_CERT')
WEBHOOK_SSL_PRIV = env.str('WEBHOOK_SSL_PRIV')
WEBAPP_HOST = env.str('WEBAPP_HOST')
WEBAPP_PORT = env.int('WEBAPP_PORT')
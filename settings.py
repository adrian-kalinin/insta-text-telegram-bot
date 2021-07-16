from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')


# bot section
BOT_TOKEN = config.get('bot', 'token')
ADMINS = tuple(map(int, config.get('bot', 'admins').split(',')))
DEVELOPER = config.getint('bot', 'developer')

# database section
DATABASE_PATH = config.get('database', 'sqlite')


# server section
# HOST = 0
# PORT = 0

# webhook
# webhook_url = https://{host}:{port}/{token}
# key_path = webhook_data/pkey.pem
# cert_path = webhook_data/cert.pem

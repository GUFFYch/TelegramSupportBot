from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = "5935256302:AAH3Uf-nCuBqZUYa2fxGTCbcYA9BCQhUGqQ"  # Забираем значение типа str
ADMINS = "743043528"  # Тут у нас будет список из админов
IP = "localhost"  # Тоже str, но для айпи адреса хоста

support_ids = [
743043528,
]

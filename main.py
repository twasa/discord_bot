import os
import logging
from services.discord import api as discord_api

discord_bot = discord_api.BotApp()
token = os.getenv('DISCORD_TOKEN', '')
FORMAT = '{"time": %(asctime)s, "name": %(pathname)s, "level": %(levelname)s, "message": %(message)s}'
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Discord Bot starting...')
    discord_bot.run(token)

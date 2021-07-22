import logging

FORMAT = '{"time": %(asctime)s, "name": %(pathname)s, "level": %(levelname)s, "message": %(message)s}'
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

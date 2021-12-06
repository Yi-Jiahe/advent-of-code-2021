import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("info.log", mode='w')
logger.addHandler(handler)

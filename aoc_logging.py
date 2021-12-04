import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("info.log")
logger.addHandler(handler)
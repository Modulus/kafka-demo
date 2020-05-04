import datetime
import os
import logging


def get_logger(name="default"):
    logging_format = "%(lineno)d in %(filename)s at %(asctime)s: %(message)s"
    logging.basicConfig(format=logging_format)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger


def stamp_message(message, fmt='%Y-%m-%d-%H-%M-%S Message: {message}'):
    return datetime.datetime.now().strftime(fmt).format(message=message)


def get_timestamp(fmt='%Y-%m-%d-%H-%M-%S'):
    return datetime.datetime.now().strftime(fmt)


def extract_bootstrap_servers():
    logger = get_logger("util")
    try:
        s_raw = os.environ["BOOTSTRAP_SERVERS"]

        return s_raw.split(",")
    except KeyError as err:
        logger.warning(f"Failed to read BOOTSTRAP_SERVERS from env. Setting to 127.0.0.1:9092")
        return ["127.0.0.1:9092"]
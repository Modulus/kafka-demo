import time
import datetime
import json
import base64
from kafka import KafkaProducer
from util import stamp_message, get_timestamp

import requests

from generated.message_pb2 import Message

import logging
# ERROR_FORMAT = "%(levelname)s at %(asctime)s in %(funcName)s in %(filename) at line %(lineno)d: %(message)s"
FORMAT = "%(lineno)d in %(filename)s at %(asctime)s: %(message)s"

logging.basicConfig(format=FORMAT)
logger = logging.getLogger("Producer")
logger.setLevel(logging.DEBUG)


def fetch_lorem():
    url = "http://loremricksum.com/api/?paragraphs=1&quotes=1"
    logger.info(f"Fetching lorem ipsum from: {url}")

    message = Message()

    response = requests.get(url)


    if response.status_code >= 200:
        logger.info("Response ok, mappaing data")
        logger.info(f"Got: {response.text}")

        data = json.loads(response.text)
        logger.info(f"Response: {data}")

        message.content = data["data"][0]
        message.timeStamp = get_timestamp()


        logger.info(f"Returning: '{message}")
        return message
         

    else:
        logger.error("Failed to get data, returning None!")
        return None


producer = KafkaProducer(bootstrap_servers="127.0.0.1:9092")
while True:
    message = fetch_lorem()
    producer.send("topic01", message.SerializeToString())
    producer.flush()
    time.sleep(4)
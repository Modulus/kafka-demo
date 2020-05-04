import datetime
import base64
import logging
from kafka import KafkaConsumer


from generated.message_pb2 import Message

FORMAT = "%(lineno)d in %(filename)s at %(asctime)s: %(message)s"

logging.basicConfig(format=FORMAT)
logger = logging.getLogger("Producer")
logger.setLevel(logging.DEBUG)




consumer = KafkaConsumer("topic01", bootstrap_servers="127.0.0.1:9092")
for msg in consumer:
    logger.info(f"Received this : {msg}")

    logger.info("Parsing content")
    message = Message()
    message.ParseFromString(msg.value)
    logger.info(f"Parsed: {message}")

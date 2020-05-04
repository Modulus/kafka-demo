import time
from kafka import KafkaConsumer
from util import get_logger, extract_bootstrap_servers


from generated.message_pb2 import Message


class MessageConsumer(object):
    def __init__(self):
        self.logger = get_logger("MessageConsumer")
        self.servers = extract_bootstrap_servers()
        self.logger.debug(f"Found servers: {self.servers}")

    def consume_messages(self):
        kafka_consumer = KafkaConsumer("topic01", bootstrap_servers=self.servers)
        for msg in kafka_consumer:
            self.logger.debug(f"Received this : {msg}")

            self.logger.debug("Parsing content")
            message = Message()
            message.ParseFromString(msg.value)
            self.logger.info(f"Parsed: [{message}]")


consumer = MessageConsumer()
consumer.consume_messages()

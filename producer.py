import time
import datetime
import json
import base64
import os
from kafka import KafkaProducer, errors
from util import stamp_message, get_timestamp, get_logger, extract_bootstrap_servers

import requests

from generated.message_pb2 import Message

import logging


class MessageProducer(object):
    def __init__(self):
        self.servers = extract_bootstrap_servers()
        self.logger = get_logger("MessageProducer")
        self.logger.info(f"Found servers: {self.servers}")

    def produce_messages(self):
        kafka_producer = KafkaProducer(bootstrap_servers=self.servers)
        while True:
            message = self._fetch_lorem()
            try:
                self.logger.info(f"Sending: [{message}]")
                kafka_producer.send("topic01", message.SerializeToString())
                kafka_producer.flush()
                time.sleep(4)
            except errors.NoBrokersAvailable:
                self.logger.error("Failed to find any brokers!")

    def _fetch_lorem(self):
        url = "http://loremricksum.com/api/?paragraphs=1&quotes=1"

        self.logger.info(f"Fetching lorem ipsum from: {url}")

        message = Message()

        response = requests.get(url)

        if response.status_code >= 200:
            self.logger.debug("Response ok, mapping data")
            self.logger.debug(f"Got: {response.text}")

            data = json.loads(response.text)
            self.logger.debug(f"Response: {data}")

            message.content = data["data"][0]
            message.timeStamp = get_timestamp()

            self.logger.debug(f"Returning: '{message}")
            return message

        else:
            self.logger.error("Failed to get data, returning None!")
            return None


producer = MessageProducer()
producer.produce_messages()

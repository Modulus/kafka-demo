import time

from kafka import KafkaProducer
from util import stampMessage


producer = KafkaProducer(bootstrap_servers="127.0.0.1:9092")
while True:
    message = "Message" #stampMessage("Hello there, how are ye?")
    print("Sending message: {}", message)
    producer.send("topic01", b"{message}")
    producer.flush()
    time.sleep(4)
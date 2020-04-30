import datetime
from kafka import KafkaConsumer


consumer = KafkaConsumer("topic01", bootstrap_servers="127.0.0.1:9092")
for msg in consumer:
    print(msg)

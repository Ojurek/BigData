import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'bitCoins',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('ascii')))

for message in consumer:
    #parsed_json = json.load(message)
    print("**********")
    print(message)
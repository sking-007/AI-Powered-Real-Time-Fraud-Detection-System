from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

while True:
    transaction = {
        "user_id": random.randint(1000, 9999),
        "amount": round(random.uniform(10, 5000), 2),
        "location": random.choice(["USA", "Germany", "India"]),
        "timestamp": time.time()
    }
    producer.send('transactions', value=transaction)
    print(f"Sent transaction: {transaction}")
    time.sleep(2)

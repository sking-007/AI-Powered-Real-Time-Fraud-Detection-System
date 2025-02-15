from kafka import KafkaConsumer
import json
import pandas as pd
from config.config import KAFKA_CONFIG

consumer = KafkaConsumer(
    KAFKA_CONFIG["TOPIC"],
    bootstrap_servers=KAFKA_CONFIG["BOOTSTRAP_SERVERS"],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_transactions():
    transactions = []
    for message in consumer:
        transaction = message.value
        transactions.append(transaction)
        print(f"Received: {transaction}")
        
        if len(transactions) >= 10:  # Save every 10 transactions
            df = pd.DataFrame(transactions)
            df.to_csv("data/raw_transactions.csv", mode="a", header=False, index=False)
            transactions = []

consume_transactions()

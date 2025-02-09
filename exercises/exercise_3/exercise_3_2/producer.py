from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

def main():
    # Anger sökvägen till orders.jsonsom ligger i samma mapp som detta skript
    data_path = Path(__file__).parent
    with open(data_path / "orders.json", "r", encoding="utf-8") as file:
        orders = json.load(file)

    # Skapa en Application-instans som ansluter till Kafka-brokern
    app = Application(broker_address="localhost:9092", consumer_group="order-producer")
    
    # Skapa en topic-referens för "orders_topic" med JSON-serialisering
    orders_topic = app.topic(name="orders_topic", value_serializer="json")
    
    # Använd producenten från app.get_producer() för att skicka meddelanden
    with app.get_producer() as producer:
        for order in orders:
            # Serialisera meddelandet. Här använder vi order_id som nyckel.
            kafka_msg = orders_topic.serialize(key=order["order_id"], value=order)
            
            # Skriv ut meddelandet för verifiering
            print(f"Produced Message; Key = {kafka_msg.key}, Value = {kafka_msg.value}")
            
            # Producera meddelandet till topicen "orders_topic"
            producer.produce(topic="orders_topic", key=str(kafka_msg.key), value=kafka_msg.value)

if __name__ == "__main__":
    pprint("Starting producer...")
    main()
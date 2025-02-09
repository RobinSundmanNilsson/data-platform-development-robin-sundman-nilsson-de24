from quixstreams import Application
import json

# Skapa applikationen med dina inställningar
app = Application(
    broker_address="localhost:9092",
    consumer_group="order-consumer",
    auto_offset_reset="earliest",
)

# Skapa en topic-referens för "orders_topic"
orders_topic = app.topic(name="orders_topic", value_deserializer="json")

# Skapa en DataFrame kopplad till topicen
sdf = app.dataframe(topic=orders_topic)

# Definiera en funktion som processar varje order
def process_order(order):
    # order är ett dictionary med order-information
    print(f"Order ID: {order['order_id']}")
    print(f"Customer: {order['customer']}")
    print("Products:")
    total_order_value = 0.0
    for product in order["products"]:
        total_price = product["price"] * product["quantity"]
        total_order_value += total_price
        print(f" - {product['name']}, {product['quantity']} st")
        print(f"   Total: {total_price:.2f} USD")
    print(f"Total order value: {total_order_value:.2f} USD")
    print("-" * 50)
    # Returnera gärna ordern om du vill fortsätta kedjan, annars kan du returnera None.
    return order

# Använd update() för att köra process_order-funktionen på varje inkommande meddelande
sdf.update(lambda order: process_order(order))

if __name__ == "__main__":
    app.run()
# 1. Explore orders data

# Use the dataset orders.json, which simulates a few orders from an electronic shop.

# a) Load the json file, read it in and try to understand the data.

# b) Use python and perhaps pandas to print out each order with the product, 
# quantity, price and total price. One order could have the following output

import json
from pprint import pprint

with open ("orders.json", "r", encoding="utf-8") as file:
    orders = json.load(file)

print("-"*50)
pprint(type(orders))
print("-"*50)
pprint(orders[:2])
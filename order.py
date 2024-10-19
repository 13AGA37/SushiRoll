import json
from datetime import datetime

class Order:
    def __init__(self, dish_name, ingredients):
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_order_json(self, order_name):
        order_data = {
            "dish_name": self.dish_name,
            "ingredients": self.ingredients,
            "order_time": self.order_time
        }
        filename = f"{order_name}.json"
        with open(filename, 'w') as json_file:
            json.dump(order_data, json_file, indent=4)
        print(f"Заказ '{order_name}' успешно сохранен в файл {filename}.")

    def read_order_from_json(self, filename):
        with open(filename, 'r') as json_file:
            order_data = json.load(json_file)
        return order_data
class SushiRollController:
    def __init__(self):
        self.rolls = []

    def add_roll(self, roll):
        self.rolls.append(roll)

    def get_rolls_for_restaurant(self):
        return [{"name": roll.get_name(), "rice": roll.get_rice(), "nori": roll.get_nori(), "fillings": roll.get_fillings(), "optional_toppings": roll.get_optional_toppings()} for roll in self.rolls]

    def get_rolls_for_website(self):
        return [{"name": roll.get_name(), "description": f"{roll.get_rice()} with {', '.join(roll.get_fillings())}", "toppings": roll.get_optional_toppings()} for roll in self.rolls]

    def update_roll(self, roll_name, new_rice=None, new_nori=None, new_fillings=None, user_role=None):
        if user_role != "admin":
            raise PermissionError("Доступ запрещен. У вас нет прав для изменения роллов.")
        for roll in self.rolls:
            if roll.get_name() == roll_name:
                if new_rice:
                    roll.set_rice(new_rice)
                if new_nori:
                    roll.set_nori(new_nori)
                if new_fillings:
                    roll.set_fillings(new_fillings)
                return
        raise ValueError("Ролл не найден.")

controller = SushiRollController()

california_roll = SushiRoll("California Roll", "Sushi Rice", "Nori", ["Crab Sticks", "Avocado"], ["Egg", "Sesame Seeds"])
controller.add_roll(california_roll)

restaurant_view = controller.get_rolls_for_restaurant()
website_view = controller.get_rolls_for_website()

try:
    controller.update_roll("California Roll", new_rice="Brown Rice", user_role="admin")
except PermissionError as e:
    print(e)

print(restaurant_view)
print(website_view)

class Controller:
    def __init__(self, view):
        self.view = view
        def save_order_to_json(self, dish_name, ingredients, order_name):
            order = Order(dish_name, ingredients)
        order.create_order_json(order_name)

    def get_data_from_json(self, filename, access_level):
        if access_level == "admin":
            return self.view.get_data_from_json(filename)
        else:
            return "У вас нет прав доступа для чтения этого файла."
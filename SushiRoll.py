class SushiRoll:
    def __init__(self, name, rice, nori, fillings, optional_toppings=None):
        self._name = name
        self._rice = rice
        self._nori = nori
        self._fillings = fillings
        self._optional_toppings = optional_toppings if optional_toppings else []
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def get_rice(self):
        return self._rice
    def set_rice(self, value):
        self._rice = value
    def get_nori(self):
        return self._nori
    def set_nori(self, value):
        self._nori = value
    def get_fillings(self):
        return self._fillings
    def set_fillings(self, value):
        self._fillings = value
    def get_optional_toppings(self):
        return self._optional_toppings
    def add_optional_topping(self, topping):
        self._optional_toppings.append(topping)
    def remove_optional_topping(self, topping):
        if topping in self._optional_toppings:
            self._optional_toppings.remove(topping)
    def change_recipe(self, new_rice, new_nori, new_fillings):
        self.set_rice(new_rice)
        self.set_nori(new_nori)
        self.set_fillings(new_fillings)
def create_custom_roll(name, rice, nori, fillings, optional_toppings=None):
    if not isinstance(name, str) or not isinstance(rice, str) or not isinstance(nori, str) or not isinstance(fillings, list):
        raise ValueError("Invalid input types")
    return SushiRoll(name, rice, nori, fillings, optional_toppings)
california_roll = SushiRoll("California Roll", "Sushi Rice", "Nori", ["Crab Sticks", "Avocado"], ["Egg", "Sesame Seeds"])
california_roll.change_recipe("Brown Rice", "Seaweed", ["Smoked Salmon", "Cucumber"])
california_roll.add_optional_topping("Sriracha Sauce")
my_custom_roll = create_custom_roll("My Custom Roll", "Sticky Rice", "Seaweed", ["Salmon", "Cream Cheese"], ["Chives"])
class SushiRollController:
    # ...

    def get_rolls_for_client(self):
        return [{"name": roll.get_name(), "description": f"{roll.get_rice()} with {', '.join(roll.get_fillings())}", "price": 10.99} for roll in self.rolls]

    def get_roll_details(self, roll_name):
        for roll in self.rolls:
            if roll.get_name() == roll_name:
                return {"name": roll.get_name(), "rice": roll.get_rice(), "nori": roll.get_nori(), "fillings": roll.get_fillings(), "optional_toppings": roll.get_optional_toppings()}
        raise ValueError("Ролл не найден.")

class SushiRollController:
 def get_rolls_for_admin(self):
  return [{"name": roll.get_name(), "rice": roll.get_rice(), "nori": roll.get_nori(), "fillings": roll.get_fillings(), "optional_toppings": roll.get_optional_toppings()} for roll in self.rolls]
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
                      def delete_roll(self, roll_name, user_role=None):
                       if user_role != "admin":
                        raise PermissionError("Доступ запрещен. У вас нет прав для удаления роллов.")
                        for roll in self.rolls:
                         if roll.get_name() == roll_name:
                          self.rolls.remove(roll)
                          return
                          raise ValueError("Ролл не найден.")




class SushiRollController:
 # ...

 def get_rolls_for_client(self):
  return [
   {
    "name": roll.get_name(),
    "description": f"{roll.get_rice()} with {', '.join(roll.get_fillings())}",
    "price": 10.99
   } for roll in self.rolls
  ]

 def get_roll_details(self, roll_name):
  for roll in self.rolls:
   if roll.get_name() == roll_name:
    return {
     "name": roll.get_name(),
     "rice": roll.get_rice(),
     "nori": roll.get_nori(),
     "fillings": roll.get_fillings(),
     "optional_toppings": roll.get_optional_toppings()
    }
  raise ValueError("Ролл не найден.")

 class SushiRollController:
  # ...

  def get_rolls_for_admin(self):
   return [
    {
     "name": roll.get_name(),
     "rice": roll.get_rice(),
     "nori": roll.get_nori(),
     "fillings": roll.get_fillings(),
     "optional_toppings": roll.get_optional_toppings()
    } for roll in self.rolls
   ]

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

  def delete_roll(self, roll_name, user_role=None):
   if user_role != "admin":
    raise PermissionError("Доступ запрещен. У вас нет прав для удаления роллов.")

   for roll in self.rolls:
    if roll.get_name() == roll_name:
     self.rolls.remove(roll)
     return

   raise ValueError("Ролл не найден.")

   def create_custom_roll(name, rice, nori, fillings, optional_toppings=None):
    if not isinstance(name, str) or not isinstance(rice, str) or not isinstance(nori, str) or not isinstance(fillings,
                                                                                                             list):
     raise ValueError("Invalid input types")
    if not name or not rice or not nori or not fillings:
     raise ValueError("All fields are required")
    return SushiRoll(name, rice, nori, fillings, optional_toppings)

 class SushiRollController:
  # ...

  def update_roll(self, roll_name, new_rice=None, new_nori=None, new_fillings=None, user_role=None):
   if user_role != "admin":
    raise PermissionError("Доступ запрещен. У вас нет прав для изменения роллов.")
   if not roll_name:
    raise ValueError("Roll name is required")

   for roll in self.rolls:
    if roll.get_name() == roll_name:
     if new_rice and not isinstance(new_rice, str):
      raise ValueError("Invalid rice type")
     if new_nori and not isinstance(new_nori, str):
      raise ValueError("Invalid nori type")
     if new_fillings and not isinstance(new_fillings, list):
      raise ValueError("Invalid fillings type")

     if new_rice:
      roll.set_rice(new_rice)
     if new_nori:
      roll.set_nori(new_nori)
     if new_fillings:
      roll.set_fillings(new_fillings)
     return

   raise ValueError("Ролл не найден.")

  def delete_roll(self, roll_name, user_role=None):
   if user_role != "admin":
    raise PermissionError("Доступ запрещен. У вас нет прав для удаления роллов.")
   if not roll_name:
    raise ValueError("Roll name is required")

   for roll in self.rolls:
    if roll.get_name() == roll_name:
     self.rolls.remove(roll)
     return

   raise ValueError("Ролл не найден.")

  class View:
   def save_order_to_json(self, order_name):
    print(f"Файл '{order_name}.json' успешно сохранен.")

   def get_data_from_json(self, filename):
    order = Order("", [])
    order_data = order.read_order_from_json(filename)
    return order_data
from sushi_roll import SushiRoll, SushiRollController
import os

class SushiRollView:
    def __init__(self):
        self.controller = SushiRollController()
        self.image_directory = "images"

    def display_rolls(self):
        rolls = self.controller.get_rolls_for_restaurant()
        if not rolls:
            print("Нет доступных роллов.")
            return
        for roll in rolls:
            print(f"\nНазвание: {roll['name']}")
            print(f"Рис: {roll['rice']}")
            print(f"Нори: {roll['nori']}")
            print(f"Начинки: {', '.join(roll['fillings'])}")
            print(f"Дополнительные топпинги: {', '.join(roll['optional_toppings'])}")
            self.display_roll_image(roll['name'])

            def display_roll_image(self, roll_name):
                image_path = os.path.join(self.image_directory, f"{roll_name}.png")  # Предполагается, что изображения имеют формат PNG if os.path.exists(image_path):
            print(f"Изображение ролла '{roll_name}': [Показать изображение: {image_path}]")
        else:
            print(f"Изображение ролла '{roll_name}' не найдено.")
    def create_roll(self):
        name = input("Введите название ролла: ")
        rice = input("Введите тип риса: ")
        nori = input("Введите тип нори: ")
        fillings = input("Введите начинки (через запятую): ").split(',')
        optional_toppings = input("Введите дополнительные топпинги (через запятую): ").split(',')

        try:
            roll = SushiRoll(name, rice, nori, fillings, optional_toppings)
            self.controller.add_roll(roll)
            print(f"Ролл '{name}' успешно создан.")
        except Exception as e:
            print(f"Ошибка при создании ролла: {e}")

    def update_roll(self):
        roll_name = input("Введите название ролла для обновления: ")
        user_role = input("Введите вашу роль (admin/user): ")
        new_rice = input("Введите новый тип риса (оставьте пустым для пропуска): ")
        new_nori = input("Введите новый тип нори (оставьте пустым для пропуска): ")
        new_fillings = input("Введите новые начинки (через запятую, оставьте пустым для пропуска): ")
        new_fillings = new_fillings.split(',') if new_fillings else None
        try:
            self.controller.update_roll(roll_name, new_rice or None, new_nori or None, new_fillings or None, user_role)
            print(f"Ролл '{roll_name}' успешно обновлен.")
        except Exception as e:
            print(f"Ошибка при обновлении ролла: {e}")

    def delete_roll(self):
        roll_name = input("Введите название ролла для удаления: ")
        user_role = input("Введите вашу роль (admin/user): ")

        try:
            self.controller.delete_roll(roll_name, user_role)
            print(f"Ролл '{roll_name}' успешно удален.")
        except Exception as e:
            print(f"Ошибка при удалении ролла: {e}")

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Показать роллы")
            print("2. Создать ролл")
            print("3. Обновить ролл")
            print("4. Удалить ролл")
            print("5. Выход")
            choice = input("Выберите опцию: ")

            if choice == '1':
                self.display_rolls()
            elif choice == '2':
                self.create_roll()
            elif choice == '3':
                self.update_roll()
            elif choice == '4':
                self.delete_roll()
            elif choice == '5':
                break
            else:
                print("Неверная опция. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    view = SushiRollView()
    view.run()
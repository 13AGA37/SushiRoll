def main():
    view = View()
    controller = Controller(view)

    # Создание заказа dish_name = "Суши"
    ingredients = ["рис", "рыба", "авокадо"]
    order_name = "sushi_order"

    controller.save_order_to_json(dish_name, ingredients, order_name)

    # Чтение заказа
    access_level = "admin"  # Измените на "user", чтобы проверить отказ в доступе
    result = controller.get_data_from_json(f"{order_name}.json", access_level)

    if isinstance(result, dict):
        print("Информация о заказе:", result)
    else:
        print(result)


if __name__ == "__main__":
    main()
import json

def load_products(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_products(filename, products):
    with open(filename, 'w') as file:
        json.dump(products, file, indent=4)


products = []


def add_product():
    product_name = input("Введіть назву товару: ")

    while True:
        try:
            product_price = float(input("Введіть ціну товару: "))
            break
        except ValueError:
            print("Неправильний формат ціни. Будь ласка, введіть число.")

    products.append({"назва": product_name, "ціна": product_price})
    save_products('products.json', products)
    print(f"Товар '{product_name}' додано до списку.")

    products.append({"назва": product_name, "ціна": product_price})
    save_products('products.json', products)
    print(f"Товар '{product_name}' додано до списку.")
    print(f"Загальна кількість товарів:{len(products)}")
def calculate_total():
    total = sum(product["ціна"] for product in products)
    return total
while True:
    print("\n1. Режим користувача")
    print("2. Режим адміністратора")
    print("3. Вийти")

    choice = input("Оберіть функію (1/2/3): ")

    if choice == '1':
        while True:
            print("\n1. Додати товар")
            print("2. Розрахувати загальну суму")
            print("3. Повернутися до головного меню")

            user_choice = input("Оберіть опцію користувача (1/2/3): ")

            if user_choice == '1':
                add_product()
            elif user_choice == '2':
                total = calculate_total()
                print(f"Загальна сума покупки: {total} грн")
            elif user_choice == '3':
                break
            else:
                print("Невірний вибір. Будь ласка, введіть 1, 2 або 3.")
    elif choice == '2':
        password = input("Введіть пароль адміністратора: ")
        if password == 'admin':
            print("\n1. Додати товар")
            print("2. Вивести список товарів")

            admin_choice = input("Оберіть опцію адміністратора (1/2): ")

            if admin_choice == '1':
                add_product()
            elif admin_choice == '2':
                print("\nСписок товарів:")
                for product in products:
                    print(f"Назва: {product['назва']}, Ціна: {product['ціна']} грн")
            else:
                print("Невірний вибір. Будь ласка, введіть 1 або 2.")
        else:
            print("Невірний пароль адміністратора.")
    elif choice == '3':
        print("Дякуємо. До побачення!")
        break
    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2 або 3.")
products = load_products('products.json')

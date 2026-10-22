import os

# Щоб програма завжди шукала файли в тій самій папці, де лежить lab7.py
# (однаково працює у Visual Studio, VS Code та в терміналі)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def read_products(filename):
    """Читає файл і повертає список товарів: [назва, ціна, кількість]."""
    products = []
    # utf-8-sig читає файл і з BOM, і без нього (Visual Studio може додати BOM)
    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue  # пропускаємо порожні рядки
            name, price, quantity = line.split(",")
            products.append([name.strip(), float(price), int(quantity)])
    if len(products) == 0:
        raise ValueError("у файлі немає товарів")
    return products


try:
    # Кроки 2-3: відкриваємо products.txt, рахуємо загальну вартість кожного товару
    products = read_products("products.txt")
    print("Загальна вартість кожного товару:")
    for name, price, quantity in products:
        print(f"{name}. {price * quantity:.2f}")

    print("\n" + "=" * 30 + "\n")

    # Кроки 4-5: шукаємо товар, назву якого ввів користувач, і записуємо його у файл
    search_name = input("Введіть назву товару: ").strip()
    found = False
    for name, price, quantity in products:
        if name.lower() == search_name.lower():
            with open("product_info.txt", "w", encoding="utf-8") as output_file:
                output_file.write(f"Назва: {name}\n")
                output_file.write(f"Ціна: {price:.2f}\n")
                output_file.write(f"Кількість: {quantity}\n")
                output_file.write(f"Загальна вартість: {price * quantity:.2f}\n")
            print("Інформацію про товар записано у файл product_info.txt")
            found = True
            break
    if not found:
        print(f"Товару '{search_name}' немає у списку.")

    print("\n" + "=" * 30 + "\n")

    # Кроки 6-7: у файлі, який вказав користувач, знаходимо товар з найменшою ціною
    file_name = input("Введіть назву файлу для пошуку найдешевшого товару: ").strip()
    products = read_products(file_name)
    cheapest = products[0]
    for product in products:
        if product[1] < cheapest[1]:
            cheapest = product
    print("Товар з найменшою ціною:")
    print(f"Назва: {cheapest[0]}")
    print(f"Ціна: {cheapest[1]:.2f}")
    print(f"Кількість: {cheapest[2]}")

# Крок 8: обробка помилок
except FileNotFoundError as e:
    print(f"Помилка: файл '{e.filename}' не знайдено!")
except ValueError as e:
    print(f"Помилка: некоректні дані у файлі ({e})")
except IOError as e:
    print(f"Помилка читання/запису файлу: {e}")

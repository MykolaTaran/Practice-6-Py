def find_unique_products():
    # Введення кількості товарів та магазинів користувачем
    n = int(input("Введіть кількість товарів в наборі: "))
    m = int(input("Введіть кількість магазинів: "))

    # Ініціалізація множини продуктів
    all_products = set(range(1, n + 1))

    # Ініціалізація множин для асортименту кожного магазину
    store_assortments = []
    for i in range(m):
        assortment = set(map(int, input(f"Введіть асортимент магазину {i + 1} через пробіл: ").split()))
        store_assortments.append(assortment)

    # Знаходження множини продуктів, які відсутні в жодному магазині
    unique_products = all_products.copy()
    for assortment in store_assortments:
        unique_products -= assortment

    # Виведення результату
    print("Множина продуктів, які відсутні в жодному магазині:", unique_products)

# Виклик функції
find_unique_products()
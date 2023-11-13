def split_list_at_index_user_input():
    # Введення списку користувачем
    user_input = input("Введіть елементи списку через кому: ")
    my_list = [int(x) for x in user_input.split(",")]

    # Введення порядкового номера для розбиття
    try:
        index_to_split = int(input("Введіть порядковий номер елемента для розбиття списку: "))
    except ValueError:
        print("Некоректний ввід. Порядковий номер має бути цілим числом.")
        return

    # Розбиття списку та виведення результатів
    if 0 <= index_to_split < len(my_list):
        first_part = my_list[:index_to_split]
        second_part = my_list[index_to_split:]
        print("Перший список:", first_part)
        print("Другий список:", second_part)
    else:
        print("Невірний порядковий номер для розбиття.")

# Виклик функції
split_list_at_index_user_input()
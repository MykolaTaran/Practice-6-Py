def find_longest_word_user_input():
    # Введення списку користувачем
    user_input = input("Введіть слова списку через кому: ")
    input_list = [word.strip() for word in user_input.split(",")]

    if not input_list:
        print("Список порожній.")
        return

    # Знаходження найдовшого слова в списку
    longest_word = max(input_list, key=len)
    print(f"Найдовше слово в списку: {longest_word}")

# Виклик функції
find_longest_word_user_input()
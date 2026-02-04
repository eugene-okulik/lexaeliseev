"""Задание 1 - Угадайка"""
import random

randon_number = random.randint(1, 5)
print(randon_number)    # для тестирования

while True:
    user_input = input("Guess a number from 1 to 5. Type 'exit' to quit: ")

    if user_input == "exit":
        print("Вы вышли из программы!")
        break

    elif int(user_input) == randon_number:
        print(f"Поздравляю! Вы угадали! Загаданная цифра: {user_input}")
        break

    else:
        print("Увы, вы не угадали! Попробуйте снова!")
        continue

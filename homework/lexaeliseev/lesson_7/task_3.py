"""Задание 3"""


def example(text):
    user_input = text + input()
    user_number = user_input.split(":")[-1]
    return int(user_number) + 10

print(example("результат:"))
print(example("результат операции:"))
print(example("результат работы программы:"))

import random

""" Задание 1 """


def salary_sum():
    salary = int(input("Назовите вашу зарплату: "))
    bonus_list = [True, False]
    bonus = random.choice(bonus_list)

    if bonus:
        result = salary + (random.randrange(10, 100, 10))
        print(f"{salary}, {bonus} - '${result}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")


salary_sum()

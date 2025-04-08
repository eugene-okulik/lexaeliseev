import random


def salary_with_bonus(salary: int):
    bonus = random.choice([True, False])
    if bonus is True:
        salary_bonus = salary + random.randint(0, 1000)
        print(f"{salary}, {bonus} - '${salary_bonus}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")


salary_with_bonus(780)

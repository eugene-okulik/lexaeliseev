"""Задание на декораторы 1"""


def decorator(func):

    def wrapper(*args):
        func(*args)
        print("finished")

    return wrapper


@decorator
def upper_text(text):
    print(text.upper())


@decorator
def summa(a, b):
    print(a + b)


upper_text("тест")
summa(3, 4)

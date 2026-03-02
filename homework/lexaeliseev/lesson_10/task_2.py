"""Задание на декораторы 2"""


def repeat_me(func):

    def wrapper(value, count=2):
        for i in range(count):
            func(value)

    return wrapper


@repeat_me
def example(text):
    print(text.upper())

example("ТЕСТ", count=5)

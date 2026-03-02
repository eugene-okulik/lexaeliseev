"""Задание на декораторы 3"""


def decorator(func):

    def wrapper(first, second):
        operation = None

        if first < 0 or second < 0:
            operation = '*'

        elif first == second:
            operation = '+'

        elif first > second:
            operation = '-'

        elif first < second:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


print(calc(1, 1))
print(calc(3, 1))
print(calc(3, 200))
print(calc(-10, 2))

def decorator(func):
    def wrapper(first, second):
        operation = None
        if second < 0 or first < 0:
            operation = "*"

        elif first == second:
            operation = "+"

        elif first > second:
            operation = "-"
            first, second = second, first

        elif second > first:
            operation = "/"

        return func(first, second, operation)

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        result = first + second

    elif operation == '-':
        result = first - second

    elif operation == '*':
        result = first * second

    elif operation == '/':
        result = first / second

    else:
        raise ValueError("Operation is invalid")

    return result


print(calc(1, 1))
print(calc(10, 1))
print(calc(10, 100))
print(calc(-10, -100))

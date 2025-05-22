def decorator(func):
    def wrapper(first, second, operation):
        # func(first, second, operation)
        result = func(first, second, operation)
        if second < 0 or first < 0:
            return first * second
        elif first == second:
            return first + second
        elif first > second:
            return first - second
        elif second > first:
            return first / second
        # elif first < 0 or second < 0:
        #     return first * second
        return result
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


print(calc(1, 1, '-'))
print(calc(10, 1, '*'))
print(calc(10, 100, '*'))
print(calc(-10, -100, '/'))

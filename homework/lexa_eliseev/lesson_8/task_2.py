import sys


sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_number_from_fibonacci(n):
    fib_generator = fibonacci_generator()
    count = 0
    fibonacci_number = 0
    for fib in fib_generator:
        if count == n:
            fibonacci_number = fib
            break
        count += 1
    return fibonacci_number


print(get_number_from_fibonacci(5), end='\n\n\n')
print(get_number_from_fibonacci(200), end='\n\n\n')
print(get_number_from_fibonacci(1000), end='\n\n\n')
print(get_number_from_fibonacci(100000))
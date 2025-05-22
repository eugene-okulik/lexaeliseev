def repeat_me(func):

    def wrapper(*args, count=1):
        for i in range(count):
            print(f"started count: {i+1}")
            func(*args)
    return wrapper


@repeat_me
def example(*text):
    print(*text)

example("started", "\nfinished\n-----", count=3)

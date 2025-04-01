value = 4
while True:
    result = input("Пожалуйста, угадайте цифру от 0 до 9: ")
    if result == value:
        print("Поздравляю! Вы угадали!")
    elif result == "Exit" or result == "exit":
        break
    else:
        print("Попробуйте снова! Если вы хотите выйти из программы введите 'Exit'")

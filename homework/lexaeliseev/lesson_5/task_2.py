"""Задание 2"""

number_input_1 = input("Введите целое число: ")

result_1 = f"результат операции: {number_input_1}"
result_index = result_1.index(":")
result = result_1[result_index:]
result_number = (result.replace(":", " ").replace(" ", ""))
result = int(result_number) + 10
print(result)

number_input_2 = input("Введите целое число: ")

result_2 = f"результат операции: {number_input_2}"
result_index = result_2.index(":")
result = result_2[result_index:]
result_number = (result.replace(":", " ").replace(" ", ""))
result = int(result_number) + 10
print(result)

number_input_3 = input("Введите целое число: ")

result_3 = f"результат работы программы: {number_input_3}"
result_index = result_3.index(":")
result = result_3[result_index:]
result_number = (result.replace(":", " ").replace(" ", ""))
result = int(result_number) + 10
print(result)

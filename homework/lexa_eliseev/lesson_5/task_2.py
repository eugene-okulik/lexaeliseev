first_value = 'результат операции: ' + input()
first_value_index = first_value.index(': ')
result = first_value[first_value_index + 2:]
print(int(result) + 10)

second_value = 'результат операции: ' + input()
second_value_index = second_value.index(': ')
result = second_value[second_value_index + 2:]
print(int(result) + 10)

third_value = 'результат работы программы: ' + input()
third_value_index = third_value.index(': ')
result = third_value[third_value_index + 2:]
print(int(result) + 10)

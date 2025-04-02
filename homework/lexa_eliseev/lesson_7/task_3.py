def concatenate_and_modify(text):
    concatenated_text = text + input()
    concatenated_text_split = concatenated_text.split(':')
    print(int(concatenated_text_split[1].strip()) + 10)


concatenate_and_modify("результат операции:")
concatenate_and_modify("результат работы программы:")
concatenate_and_modify("результат:")

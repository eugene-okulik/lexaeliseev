example = '“Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”'

text = example.split()

symbol = ['.', ',', '”']
result = []

for word in text:
    if word[-1] in symbol:
        value_word = word[:-1] + 'ing' + word[-1]
        result.append(value_word)
    else:
        value_word = word + 'ing'
        result.append(value_word)
print(' '.join(result))

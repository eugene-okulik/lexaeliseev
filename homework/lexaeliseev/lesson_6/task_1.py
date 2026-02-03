"""Задание 1"""

text = "“Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”"

new_text = text.split()

new_list = []
symbol = [",", ".", "”"]

for word in new_text:
    if word[-1] in symbol:
        new_world = word[:-1] + "ing" + word[-1]
        new_list.append(new_world)
    else:
        new_list.append(word + "ing")
print(new_list)

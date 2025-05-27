PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = {}

data = PRICE_LIST.split('\n')
print(data)

for i in data:
    key, value = i.split()
    new_list[key] = int(value[:-1])

print(new_list)

"""dict comprehension"""
new_dict = {i.split()[0]: int(i.split()[1][:-1]) for i in data}

print(new_dict)

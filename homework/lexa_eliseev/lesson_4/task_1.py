my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [6, 7, 8, 9, 10],
           'dict': {1: 1, 2: 2, 'hello': 'hello', 4: 4, 5: 5},
           'set': {11, 12, 13, 14, 15}}

print(my_dict['tuple'][-1])

my_dict['list'].append(999)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'i am a tuple'
my_dict['dict'].pop(('i am a tuple',))

my_dict['set'].add(000)
my_dict['set'].remove(000)

print(my_dict)

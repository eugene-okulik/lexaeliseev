temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

""" Стандартный способ """
days_list = []
for i in temperatures:
    if i > 28:
        days_list.append(i)

print(max(days_list))
print(min(days_list))
print(round(sum(days_list) / len(days_list)),)

""" FILTER """


def filter_hot_days(x):
    return x > 28


days_list = list(filter(filter_hot_days, temperatures))
print(max(days_list))
print(min(days_list))
print(round(sum(days_list) / len(days_list)),)

""" FILTER + LAMBDA """
days_list = list(filter(lambda x: x > 28, temperatures))
print(max(days_list))
print(min(days_list))
print(round(sum(days_list) / len(days_list)),)

""" Вариант 1"""

import os
import datetime

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
new_path = os.path.join(path, "eugene_okulik", "hw_13", "data.txt")


new_list = []
with open(new_path, "r") as file:
    for i in file:
        result = i.strip()
        new_list.append(result)


data1 = new_list[0][3:29]
data1 = datetime.datetime.strptime(data1, "%Y-%m-%d %H:%M:%S.%f")
print(data1 + datetime.timedelta(days=7))

data2 = new_list[1][3:29]
data2 = datetime.datetime.strptime(data2, "%Y-%m-%d %H:%M:%S.%f")
print(data2.weekday())
print(data2.strftime("%A"))


data3 = new_list[2][3:29]
data3 = datetime.datetime.strptime(data3, "%Y-%m-%d %H:%M:%S.%f")
print(datetime.datetime.now() - data3)

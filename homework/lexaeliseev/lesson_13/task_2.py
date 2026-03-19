""" Вариант 2"""

import os
import datetime

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
new_path = os.path.join(path, "eugene_okulik", "hw_13", "data.txt")


def get_date(index_line):
    with open(new_path, "r") as file:
        lines = file.readlines()

        line = lines[index_line].strip("\n")
        date_line = line[3:29]
        return datetime.datetime.strptime(date_line, "%Y-%m-%d %H:%M:%S.%f")


data1 = get_date(0)
print(data1 + datetime.timedelta(days=7))

data_2 = get_date(1)
print(data_2.weekday())
print(data_2.strftime("%A"))

data_3 = get_date(2)
print(datetime.datetime.now() - data_3)

from datetime import datetime

example_date = "Jan 15, 2023 - 12:05:33"
python_time = datetime.strptime(example_date, '%b %d, %Y - %I:%M:%S')

month_name = python_time.strftime('%B')
print(month_name)

new_format = '%d.%m.%Y, %H:%M'
new_python_time = datetime.strftime(python_time, new_format)
print(new_python_time)

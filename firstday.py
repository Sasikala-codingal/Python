from datetime import datetime


today = datetime.today()

first_day_of_month = today.replace(day=1)


print(first_day_of_month)
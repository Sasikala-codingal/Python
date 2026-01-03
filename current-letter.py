import datetime

now = datetime.datetime.now()


current_weekday_abbr = now.strftime("%a")
current_letter = current_weekday_abbr[0]

print(f"The first letter of the current weekday is: {current_letter}")
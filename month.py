import calendar


for i in range(1,13):
  

  if i>0:
    month_name = calendar.month_name[i]
    print(f"The name of month {i} is: {month_name}")
    i+=1
  else:
    print("Invalid month number")
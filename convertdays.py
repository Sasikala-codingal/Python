print("COUNTING THE NUMBER OF DAYS")
days=int(input("Enter the number of days:"))
years=days//365
week=(days%365)//7
days=(days%365)%7
print("Number of years:",years) 
print("Number of weeks:",week)
print("Number of days:",days)   
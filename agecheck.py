print("Welcome to the Age Checker!")
age = int(input("Please enter your age: "))
if age > 10:
    if age < 20:
        print("You have eligible age.")
    else:
        print("You are too old.")
else:
    print("You are too young.")
print()
print("Thank you for using the Age Checker!")
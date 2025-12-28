a = float(input("Enter the base number: "))
b = int(input("Enter the power: "))

result = 1
for i in range(b):
    result *= a

print(f"'{a}' raised to the power '{b}' is: '{result}'")
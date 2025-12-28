a = int(input("Enter a decimal number: "))
b = ""


while a > 0:
    rem= a % 2
    a = a // 2

    
    temp = ""
    for i in range(len(b)):
        temp += b[i]

    b = str(rem) + temp

print("Binary:", b)
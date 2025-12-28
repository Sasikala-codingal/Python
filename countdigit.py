num = int(input("Enter a number: "))

a = 0
n = abs(num)     
if n == 0:
    a = 1
else:
    while n > 0:
        n //= 10  
        a += 1

print("Total digits:", a)
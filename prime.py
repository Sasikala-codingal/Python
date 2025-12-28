low_range=int(input("Enter the lower range to find prime numbers: "))
high_range=int(input("Enter the higher range to find prime numbers: "))
for num in range(low_range, high_range + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
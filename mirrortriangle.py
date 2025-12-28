n = int(input("Enter the Number of rows"))

for i in range(1, n + 1):
   left = "*" * i
   spaces = " " * (2 * (n - i))
   right = "*" * i
   print(left + spaces + right)
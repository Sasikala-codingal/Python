n=int(input("Enter the value of numbers to sum:"))
sum=0
for i in range(0,n+1,5):
    sum=sum+i
    print(sum)
print("THe total is ", sum)

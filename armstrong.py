n=int(input("Enter the numnber to find the armstrong number or not"))
i=0
sum=0
n2=n
while n2>0:
    d=n2%10
    sum+=d**3
    n2//=10
    i=i+1
if n==sum:
    print("It is an anrmstrong number")
else:
     print("It is not an anrmstrong number")
print("THe number of digits is ",i)


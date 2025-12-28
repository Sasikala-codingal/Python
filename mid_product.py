n=int(input("Enter the number:"))
t= n
len=0
while t>0:
    len=len+1
    t=int(t//10)
    print(t)
if len>=4:
    len=int(len/2)
    chk=0
    while n>0:
        rem=n%10
        if chk==len:
            midone=rem
        elif chk==len-1:
            midtwo=rem
        n=int(n//10)
        chk=chk+1
    mid_product=midone*midtwo  
    print("The product of middle two digits is:",mid_product)   
else:
    print("The number does not have middle two digits")
s=input("Enter a word to find the repeated letter")
c=input("Enter the character to count the repetetion")
i=0
count=0
print("The length is " , len(s))
while (i<len(s)): 
    print(s[i])
    if s[i]==c:
        print(s[i])
        count=count+1
    i=i+1
print("The character",c,"has repeated",count,"times in the word",s) 
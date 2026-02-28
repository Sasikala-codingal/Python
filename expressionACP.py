class expression:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    
    def add(self):
        return self.num1 + self.num2 + self.num3
        
#main program
print("Solve expressions")
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
obj=expression(n1,n2,n3)

print("Addition:",obj.add())
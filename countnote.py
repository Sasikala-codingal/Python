print("Program to find the number of notes to Withdraw from ATM")
amount=int(input("Enter the amount:"))
note_100=amount/100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10
print("Number of 100 notes:",int(note_100)) 
print("Number of 50 notes:",int(note_50))
print("Number of 10 notes:",int(note_10))


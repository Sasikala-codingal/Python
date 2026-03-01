# Initialize dictionary
math_mark = {'Ram' : 90, 'Anu' : 94, 'Vikram ' : 90, 'Ramya' : 90 , 'riya' : 100}
  
# printing original dictionary
print("The original dictionary : " +  str(math_mark))
  
# Initialize value 
K = 90
  
# Using loop
# Selective key values in dictionary
res = 0
for key in math_mark:
    if math_mark[key] == K:
        res = res + 1
      
# printing result 
print("Frequency of 90 in the dictionary is : " + str(res))


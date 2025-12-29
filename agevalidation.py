def validate_age(age_input):
   
    try:
    
        age = int(age_input)
        if 0 <= age <= 120:
            return (f"The age {age} is valid.")
        elif age < 0:
        
            raise ValueError("Age cannot be a negative number.")
        else:
        
            raise ValueError(f"The age {age} is unrealistic (must be <= 120).")

    except ValueError as e:
     
        return f"Error: {e}"
    except Exception as e:
 
        return f"An unexpected error occurred: {e}"
print("Testing age validation function:")
age=input("Enter age to validate: ")
validate_age(age)
if(age%2==0):
    print("Even age entered.")
else:
    print("Odd age entered.")


# Prompt the user for input
input = input("Enter a single character: ")

# Check if the input is exactly one character long
if len(input) == 1:
    # Get the ASCII value using ord()
    ascii_value = ord(input)
    # Print the result
    print(f"The ASCII value of '{input}' is {ascii_value}")
else:
    print("Invalid input. Please enter only one character.")
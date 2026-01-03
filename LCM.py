import math

def calculate_lcm(a, b):
    """Calculates the LCM of two positive integers using their GCD."""
    
    return abs(a * b) // math.gcd(a, b)

def main():
    print("--- LCM Calculator ---")
    while True:
        try:
            num1_str = input("Enter the first number: ")
            num2_str = input("Enter the second number: ")

            num1 = int(num1_str)
            num2 = int(num2_str)

            if num1 <= 0 or num2 <= 0:
                raise ValueError("Numbers must be positive integers.")

            lcm_result = calculate_lcm(num1, num2)
            print(f"The LCM of {num1} and {num2} is: {lcm_result}")
            break 

        except ValueError as e:
            
            print(f"Error: {e}. Please enter valid positive integers.")
        except Exception as e:
            
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
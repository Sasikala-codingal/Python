def mirror_chars(s):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    mirror_map = dict(zip(original, reverse)) # Create the mirror lookup dictionary

    mirrored_string = ""
    for char in s:
        # Use .get() to handle characters not in the map (e.g., spaces, numbers)
        mirrored_string += mirror_map.get(char, char) 
        
    return mirrored_string

# Example usage:
input_string =input("Enter a string to get mirror string:")
result = mirror_chars(input_string)
print(f"Original: {input_string}")
print(f"Mirrored: {result}")

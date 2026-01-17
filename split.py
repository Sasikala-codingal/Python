my_list = [1, 2, 3, 4, 5, 6, 7]

# Calculate the midpoint index
mid_index = len(my_list) // 2

# Split the list into two halves
first_half = my_list[:mid_index]  # Elements from the start up to (but not including) the midpoint
second_half = my_list[mid_index:] # Elements from the midpoint to the end

print(f"Original list: {my_list}")
print(f"First half: {first_half}")
print(f"Second half: {second_half}")
def circumference(radius):
    pi = 3.14159
    circum= 2 * pi * radius
    return circum
print("CALCULATING CIRCUMFERENCE OF A CIRCLE")
r = float(input("Enter the radius of the circle: "))
result = circumference(r)
print("The circumference of the circle is:", result)    
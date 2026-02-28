def test(lst):
    result = []
    for item in lst:
        result.append(list(item)) #converts each tuple into list
    return result

students=((1,"Riya","VIII"),(2,"Renu","VIII"),(3,"Akash","VIII"),(4,"Viki","VIII"))

print("\noriginal tuple:")
print(students)
print("\nconverted tuple to list:")
print(test(students))
    
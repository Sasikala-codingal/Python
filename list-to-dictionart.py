def test(lst):
	result = {}
	for item in lst:
		result[item[0]] = item[1:]
		print("result ", result)
	return result

students = [[1, 'Jean', 'V'], [2, 'LILY', 'V'], [3, 'Brian', 'VI'], [4, 'Foster', 'VI'], [5, 'Simon', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted  lists to a dictionary:")
print(test(students))
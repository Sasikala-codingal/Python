# Create from a list
my_list = [1, 2, 3, 3, 4]
frozen_set = frozenset(my_list)
print(frozen_set)


# Create from a dictionary (uses only keys)
student = {"Name": "John", "Age": "25"}
frozen_keys = frozenset(student)
print(frozen_keys)


# Create an empty frozenset
empty_frozen = frozenset()
print(empty_frozen)


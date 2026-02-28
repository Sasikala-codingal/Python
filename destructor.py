class fruit:
    name="Mango"
    # Deleting (calling destructor)
    def __del__(self):
        print('Destructor called, fruit object is deleted.')

obj = fruit()
print(obj.name)
del obj
print(obj.name)  # This will raise an error since obj is deleted

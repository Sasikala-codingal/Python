# create class
class Vehicle:

	# create init method
    def __init__(self, max_speed, mileage):

		# bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
modelX = Vehicle(240, 18)
modelY = Vehicle(250, 20)

# access the variables inside init method
print("ModelX Max Speed:",modelX.max_speed)
print("ModelX Mileage:", modelX.mileage)
print("ModelY Max Speed:",modelY.max_speed)
print("ModelY Mileage:", modelY.mileage)
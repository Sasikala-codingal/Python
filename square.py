import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(600,600)
square=turtle.Turtle()

sides=4
side_length=100
angle=360/sides

for i in range(sides):
    square.forward(side_length)
    square.right(angle)   
 
turtle.done()

import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(600,600)
polygon=turtle.Turtle()

sides=6
side_length=80
angle=360/sides

for i in range(sides):
    polygon.forward(side_length)
    polygon.right(angle)   


 
turtle.done()

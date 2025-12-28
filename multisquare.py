import turtle
mpen=turtle.Turtle()
sq=turtle.Screen()
sq.bgcolor("blue")  
size=0
while True:
    for i in range(4):
        mpen.fd(size+1)
        mpen.left(90)
        size=size-5
    size=size+1
turtle.done()


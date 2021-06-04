# This is a snowflake drawn using turtle. I have named the turtle Aisling.
import turtle
import random
aisling = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colours = ["cyan", "purple", "white", "blue"]
aisling.penup()
aisling.forward(90)
aisling.left(45)
aisling.pendown()
def branch():
    for i in range(3):
        for i in range(3):
            aisling.forward(30)
            aisling.backward(30)
            aisling.right(45)
        aisling.left(90)
        aisling.backward(30)
        aisling.left(45)
    aisling.right(90)
    aisling.forward(90)
    aisling.color(random.choice(colours))
for i in range(8):
    branch()
    aisling.left(45)
#    aisling.color(random.choice(colours))
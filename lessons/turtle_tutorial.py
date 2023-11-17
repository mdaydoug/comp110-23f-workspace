"""Setting Up the Turtle."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()
side_length: int = 300

colormode(255)

leo.color(174, 171, 170)
leo.penup()
leo.goto(-120, -60)
leo.pendown()
leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob.color(0, 0, 0)
bob.speed(70)

bob.penup()
bob.goto(-120, -60)
bob.pendown()
bob.hideturtle()

i: int = 0
while (i < 180):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122.22)
    i = i + 1
done()
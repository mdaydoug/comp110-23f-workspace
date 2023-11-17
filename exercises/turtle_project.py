"""Happy Sunglasses Emoji."""

__author__ = "730660951"

from turtle import Turtle, done


def main() -> None:
    """The canvas of my Turtle Masterpiece.

    I drew glasses twice (Lines 23 and 25) and I drew eyebrow twice (Lines 25 and 26).
    """
    #  Declare Turtle Variables here
    don: Turtle = Turtle()
    rafa: Turtle = Turtle()
    angelo: Turtle = Turtle()
    leo: Turtle = Turtle()
    #  Call procedures I define and pass Turtle as an argument.
    draw_circle(don, 260, 0, -240)
    draw_glasses(rafa, -160, 140, 130)
    draw_nose(rafa, -30, 140, 60)
    draw_glasses(rafa, 30, 140, 130)  
    draw_smile(angelo, 120, 0, -60)
    draw_eyebrow(leo, -140, 160, 100, 10)
    draw_eyebrow(leo, 40, 160, 100, 10)
    done()

#  Define procedures for other components in scene


def draw_circle(don: Turtle, radius: float, x: float, y: float) -> None:
    """Draw a circle with given radius whose center is located at point x, y.

    Circles are fun and are not something we used in the turtle tutorial. 
    I used a different fill color (Line 40) and also used a different marker color (Line 40).
    """
    don.penup()
    don.goto(x, y)
    don.pendown()
    don.hideturtle()
    don.color("orange", "yellow")
    don.begin_fill()
    don.circle(radius)
    don.end_fill()


def draw_glasses(rafa: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top left corner is located at point x, y, and then gets drawn twice.

    I also used a while loop in this function (Line 55).
    """
    rafa.penup()
    rafa.goto(x, y)
    rafa.pendown()
    rafa.hideturtle()
    i: int = 0
    rafa.begin_fill()
    while i < 4:
        rafa.forward(width)
        rafa.right(90)
        i += 1
    rafa.end_fill()


def draw_nose(rafa: Turtle, x: float, y: float, width: float) -> None:
    """Draw a horizontal line of the given width starting at x, y.

    The draw_nose function breaks up the complexity of the draw_glasses function (Lines 62-66).
    """
    rafa.goto(x, y)
    rafa.forward(width)


def draw_smile(angelo: Turtle, radius: float, x: float, y: float) -> None:
    """Draw a semi-circle with given radius whose "center" is located at point x, y.

    Semi-circles were not in the tutorial and utilize another parameter than circles, like extent (Line 82). 
    Marker Color (Line 77).
    """
    angelo.penup()
    angelo.goto(x, y)
    angelo.pendown()
    angelo.hideturtle()
    angelo.color("red", "white")
    angelo.begin_fill()
    angelo.forward(radius)
    angelo.right(-270)
    # The second argument of angelo.circle is the extent (180 to make it a semi-circle)
    angelo.circle(-radius, 180)
    angelo.right(90)
    angelo.forward(radius)
    angelo.end_fill()


def draw_eyebrow(leo: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of the given width and length whose top left- corner is located at x, y.

    Used a for loop (Line 97).
    """
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.hideturtle()
    idx: int = 0
    leo.begin_fill()
    for idx in range(2):
        leo.forward(width)
        leo.right(90)
        leo.forward(length)
        leo.right(90)
    leo.end_fill()


if __name__ == "__main__":
    main()

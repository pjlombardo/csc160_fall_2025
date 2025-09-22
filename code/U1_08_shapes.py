'''
File:       U1_08_shapes.py
Author:     P. Lombardo
Date:       ...
Purpose:    In this program we review some good programming practices,
            and incorporate our own functions with turtle graphics.
'''
import turtle

# Improve: remove magic numbers
# introduce global variables
FORWARD_LENGTH = 50
PENTAGRAM_ANGLE= 2*72
PENTAGON_TURN_ANGLE = 72
PENTAGRAM_LENGTH = 80

def draw_pentagon(turtle):
    """Draws a pentagon on the canvas
    Parameters:
        turtle (turtle object)
    Return: None
    """
    turtle.forward(FORWARD_LENGTH)
    turtle.left(PENTAGON_TURN_ANGLE)
    turtle.forward(FORWARD_LENGTH)
    turtle.left(PENTAGON_TURN_ANGLE)
    turtle.forward(FORWARD_LENGTH)
    turtle.left(PENTAGON_TURN_ANGLE)
    turtle.forward(FORWARD_LENGTH)
    turtle.left(PENTAGON_TURN_ANGLE)
    turtle.forward(FORWARD_LENGTH)
    turtle.left(PENTAGON_TURN_ANGLE)
    return None

def draw_pentagram(turtle):
    turtle.left(PENTAGON_TURN_ANGLE)
    turtle.forward(PENTAGRAM_LENGTH)
    turtle.right(PENTAGRAM_ANGLE)
    turtle.forward(PENTAGRAM_LENGTH)
    turtle.right(PENTAGRAM_ANGLE)
    turtle.forward(PENTAGRAM_LENGTH)
    turtle.right(PENTAGRAM_ANGLE)
    turtle.forward(PENTAGRAM_LENGTH)
    turtle.right(PENTAGRAM_ANGLE)
    turtle.forward(PENTAGRAM_LENGTH)
    return None

# Can we make the pentagram fit perfectly with corners
# of the pentagon?


def main():
    pat = turtle.Turtle()
    pat.color("red")
    screen = pat.getscreen()

    # How can we make the turtle draw a pentagon 
    draw_pentagon(pat)
    draw_pentagram(pat)


    
    screen.mainloop()

main()
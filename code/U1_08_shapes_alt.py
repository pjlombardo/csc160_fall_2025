'''
File:       U1_08_shapes_alt.py
Author:     P. Lombardo
Date:       ...
Purpose:    In this program we review some good programming practices,
            and incorporate our own functions with turtle graphics.
            This "alternative" version shows a way to avoid global variables
            by defining the variables in main and passing them as needed
            to functions as arguments for parameters.
'''
import turtle

# Improve: remove magic numbers
# introduce global variables

def draw_pentagon(turtle, FORWARD_LENGTH_param, PENTAGON_TURN_ANGLE_param):
    """Draws a pentagon on the canvas
    Parameters:
        turtle (turtle object)
    Return: None
    """
    turtle.forward(FORWARD_LENGTH_param)
    turtle.left(PENTAGON_TURN_ANGLE_param)
    turtle.forward(FORWARD_LENGTH_param)
    turtle.left(PENTAGON_TURN_ANGLE_param)
    turtle.forward(FORWARD_LENGTH_param)
    turtle.left(PENTAGON_TURN_ANGLE_param)
    turtle.forward(FORWARD_LENGTH_param)
    turtle.left(PENTAGON_TURN_ANGLE_param)
    turtle.forward(FORWARD_LENGTH_param)
    turtle.left(PENTAGON_TURN_ANGLE_param)
    return None

def draw_pentagram(turtle):
    # put our code for the pentaGRAM here
    return None

# Can we make the pentagram fit perfectly with corners
# of the pentagon?


def main():
    FORWARD_LENGTH = 50
    PENTAGON_TURN_ANGLE = 45
    pat = turtle.Turtle()
    pat.color("red")
    screen = pat.getscreen()

    # How can we make the turtle draw a pentagon 
    draw_pentagon(pat, FORWARD_LENGTH, PENTAGON_TURN_ANGLE)


    
    screen.mainloop()

main()
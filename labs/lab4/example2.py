"""
File:       example2.py
Author:     P. Lombardo
Date:       
Purpose:    This program uses the turtle module to draw a sequence of shapes
            where we control the color and drawing using keyboard commands.

Notes:      This program is part of a lab where we review basic computer science
            terms and practice coding. The goal is to help prepare for the first
            quiz of the semester.
"""

import turtle

def draw_square(pat,color_choice):
    """ This function uses the turtle object pat to draw a square filled in 
    with a provided color, and then move two steps forward to prepare for the next
    keyboard input.
    """
    # pause animation
    screen = pat.getscreen()
    screen.tracer(0)

    # draw square
    pat.color(color_choice)
    pat.begin_fill()
    pat.forward(FORWARD_STEP)
    pat.left(90)
    pat.forward(FORWARD_STEP)
    pat.left(90)
    pat.forward(FORWARD_STEP)
    pat.left(90)
    pat.forward(FORWARD_STEP)
    pat.end_fill()
    
    # move 
    pat.setheading(0)
    pat.penup()
    pat.forward(30)
    pat.pendown()

    screen.update()

    return None

def draw_triangle(pat, color_choice):
    """ This function uses the turtle object pat to draw a triangle filled in 
    with a provided color, and then move two steps forward to prepare for the next
    keyboard input.
    Parameters:
        pat (turtle object):  the turtle object we use to draw.
        color_choice (str): a color string either "purple" or "orchid"
    Return: None
    """
    return None

def set_listeners(pat):
    """ This function sets our keyboard and screen listeners for the program.
    Parameters: pat (turtle object)
    Return: None
    """
    screen = pat.getscreen()
    screen.onkeypress(lambda: draw_square(pat,"red"),'r')
    
    return None

def main():
    # Set side length for shapes
    FORWARD_STEP = 15

    # create screen and teleport the turtle to the left
    pat = turtle.Turtle()
    screen = pat.getscreen()
    pat.teleport(-250,0)
    
    # set keyboard listeners for user interaction
    set_listeners(pat)

    screen.listen()
    screen.mainloop()

if __name__=="__main__":
    main()
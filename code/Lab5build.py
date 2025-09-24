'''
File:       lab5build.py
Author:     P. Lombardo
Date:       ...
Purpose:    Solutions to lab 4, which implements a type of random search from
            a starting position to a globally defined "target".  The turtle can
            only move forward, left, or right, and if the turtle hits the target
            the game ends and "I made it" is printed to the screen.

Notes:      The structure of the lab activity is heavily inspired by Hank Feild's 
            original lab making a drawing palette.
            This needs documentation!
'''

import turtle
import random
import math

# Choose a step size for the movement of the turtle
STEP = 10
target = (30.0,30.0)

# random direction function
def choose_direction():
    random_num = random.random()
    if random_num <= 0.3333:
        return("left")
    elif random_num <=0.6666:
        return("forward")
    else:
        return("right")

# functions to develop
    # something to check if we've hit the target.


def move_chuck(chuck):
    screen = chuck.getscreen()
    screen.tracer(0)
    direction = choose_direction()

    if direction == "left":
        chuck.left(90)
        chuck.forward(STEP)
    elif direction == "forward":
        chuck.forward(STEP)
    else:
        chuck.right(90)
        chuck.forward(STEP)

    screen.update()


def set_listeners(chuck):
    screen = chuck.getscreen()
    screen.onkeypress(lambda: move_chuck(chuck),'Return')
    screen.onkeypress(lambda: clear_canvas(chuck),'C')


def clear_canvas(chuck):
    """Removes all objects drawn on the screen.
    """
    print('Clearing the canvas.')
    screen = chuck.getscreen()
    screen.tracer(0)
    screen.resetscreen()
    # Clearing the screen also removes all event listeners, so we have to reset
    # them all.
    set_listeners(chuck)

    # Re-draw home and start chuck there
    chuck.color('red')
    chuck.teleport(target[0],target[1])
    chuck.dot(15)
    chuck.teleport(0,0)
    chuck.color('black')
    chuck.dot(10)
    chuck.pendown()

    # modify the cursor look (just for fun :) )
    chuck.color('#a16bff')
    chuck.shapesize(1,1,1)
    screen.update()

def main():
    # global chuck, screen

    #initialize a turtle and a screen
    chuck = turtle.Turtle()
    screen = chuck.getscreen()

    # print(globals())
    
    # set Screen size in pixels
    screen.setup(1050, 732)
    screen.setworldcoordinates(-525,-358,525,358)
    
    clear_canvas(chuck)

    set_listeners(chuck)

    screen.listen()
    screen.mainloop()

main()
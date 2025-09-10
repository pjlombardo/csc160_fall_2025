'''
File:       lab3.py
Author:     ...
Date:       ...
Purpose:    In this lab we practice with functional abstraction. We write python functions 
            to control draw a compass, and control the movement of a turtle to create 
            a game where the user can manually move their way through a 
            maze.

            We also introduce the "main" function.

Notes:      Initial code by P. Lombardo, inspired by Hank Feild.
'''
 
# Imports
import turtle


# Functions

def move_east():
    """ Moves the turtle *east* on the screen, which is toward
    the right.

    Parameters:
        There are no parameters to this function, since we are
        always moving east when we call his function.
    """
    screen.tracer(0)

    # we may soon add a call to another function here...

    # Here is our code 
    pat.setheading(0)
    # Notice the amount we move forward is set by the constant variable
    # WIDTH, since we are moving a left/right.
    pat.forward(WIDTH)
    screen.update()

def move_west():
    """ Moves the turtle *west* on the screen, which is toward
    the left.

    Parameters:
        There are no parameters to this function.
    """
    return 0
    

def move_north():
    """Doc string

    Parameters:
        ...
    """
    return 0

def move_south():
    """Doc string

    Parameters:
        ...
    """
    return 0

def draw_triangle():
    """This draws a small triangle behind the turtle 
    (We use it to leave a trail of where the turtle has been).

    Parameters:
        There are no parameters for this function.
    """
    return 0

def create_maze_filename(number):
    """ This function takes in a number, and returns a string
    identifying the filename of the maze we want to use. For example,
    create_maze_filename(2) would return 'maze2.png'

    Parameters:
        number (int):   indicates the maze number of the file we want to use.
                        (This should be an integer between 0 and 5.)
    
    """
    return 0


def set_listeners():
    """ Sets listeners for various keyboard button presses.

    Parameters: None
    """
    # call the move_east() function when the right arrow is pressed.
    screen.onkeypress(move_east, 'Right')


def main():
    """Sets up the *main* part of our program. It:
        * creates a turtle and screen object
        * sets the HEIGHT and WIDTH constants
        * adds a maze background
        * sets up listeneres to respond to keyboard input

    Parameters: None.
    """
    # share the following variables and objects globally
    # so that other functions can use them.
    global pat, screen, HEIGHT, WIDTH

    # Set HEIGHT and WIDTH constants to suit the images.
    WIDTH = 30
    HEIGHT = 20

    # start with turtle and screen objects:
    pat = turtle.Turtle()
    screen = pat.getscreen()
    # set Screen size in pixels
    screen.setup(1050, 900)
    screen.setworldcoordinates(-525,-338,525,450)

    # Set the screen background
    # (We'll change this soon to make it interactive!)
    screen.bgpic("maze1.png")

    # modify the cursor look (just for fun :) )
    pat.color('#a16bff')
    pat.shapesize(2,2,1)
    pat.speed(5)


    # move turtle to the start of the maze
    pat.teleport(-512,165)
    pat.pendown()
    screen.update()

    # activiate keyboard listeners
    set_listeners()

    screen.listen()
    screen.mainloop()


if __name__=="__main__":
    main()
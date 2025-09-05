import turtle
import time

# Start a turtle object and a screen object
pat = turtle.Turtle()
screen = pat.getscreen()

# set Screen size in pixels
screen.setup(1050, 732)
screen.setworldcoordinates(-525,-358,525,358)

# modify the cursor look (just for fun :) )
pat.color('#a16bff')
pat.shapesize(2,2,1)

# set the screen background (we’ll change this soon) 
screen.bgpic("maze0.png")

# move turtle to the start
pat.penup()
pat.goto(-512,185)
time.sleep(1)
pat.speed(3)
pat.pendown()


# TODO: Place your escape algorithm goes below!

# Recommdended. Create and assign global variables HEIGHT and WIDTH
# to store what one "step" on the grid would be for the box 
# (HEIGHT and WIDTH dimensions)


# After setting these global varibles, transfer your partner's pseudocode
# into turtle movements!  Remember to test often and make sure the program
# looks like your graph paper sketch as you go.






screen.exitonclick()
screen.mainloop()

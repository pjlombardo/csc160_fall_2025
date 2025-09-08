'''
File:       U1_03_orange_volume.py
Author:     P. Lombardo
Date:       ...
Purpose:    This program asks the user for the diameter of an orange, and
            uses it to compute the volume (and surface area, eventually) 
            of an orange. Print the volume of the orange to the console.
'''

# Brainstorm your program in comments:
    # Decompose the problem
    # write some "psuedo code" for more complicated things (like finding the volume)

# constants
# need PI
PI = 3.1415


# Get diameter (must be a float)
diameter = float( input("What is the diameter of your orange? "))


# compute volume
    # assign volume = (4/3) and update with subsequent multiplications

volume = (4/3)
volume = volume * diameter / 2
volume = volume * diameter / 2
volume = volume * diameter / 2
volume = volume * PI

# print volume
print(f"Your orange has a volume of {volume}.")


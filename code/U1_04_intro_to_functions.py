'''
File:       U1_04_intro_to_functions.py
Author:     P. Lombardo
Date:       ...
Purpose:    In this program we re-write an existing program to use a function, 
            streamlining our code while also make the code more readable.
'''
# this is a module import, specfically the "math" package.
# I use this below to get the constant for pi (math.pi)
import math

# Functions

def get_diameter(circular_object):
    """Asks the user to input the diameter of their circular_object.
    Inputs: circular_object (str), name of the object
    Return: diameter (float), the diameter provided from the user.
    """
    diameter = float(input(f"What is the diameter of your {circular_object}? "))
    return diameter

# Define a function to compute the area from diameter.
def get_circle_area(diameter):
    """From a provided diameter, this computes the area of the associated
    circle.
    Inputs: diameter (float),  The provided diameter of the circular object
    Return: area (float), The area of the circular object.
    """
    area = math.pi*(diameter/2)**2
    return area

def print_circular_area(circular_object, circle_area):
    """ Print a sentence sharing the object and its area.
    Inputs:
        circular_object (str): what we call the given object
        circle_area (float):   the area of the given object
    Print: a sentence that shares the name of the object and
    its circular area. (optional)
    Return: None
    """
    print(f"Your {circular_object} has an area of {circle_area}.")
    return None

# main() this executes the program user our "helper functions"
def main():
    # get the diameters of the objects of interest
    pizza_diameter = get_diameter("pizza")
    cherry_pie_diameter = get_diameter("cherry pie")
    seat_diameter = get_diameter("seat")

    # compute areas
    pizza_area = get_circle_area(pizza_diameter)
    cherry_pie_area = get_circle_area(cherry_pie_diameter)
    seat_area = get_circle_area(seat_diameter)

    # print areas
    print_circular_area("pizza", pizza_area)
    print_circular_area("cherry pie", cherry_pie_area)
    print_circular_area("seat", seat_area)

main()

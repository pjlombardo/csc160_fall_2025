"""
File:       example1.py
Author:     P. Lombardo
Date:       
Purpose:    This program will get (x,y)-coordinates for two points from the user,
            and then compute the distance between them, as well as the area of
            an equilateral triangle with that length as the base.

Notes:      This program is part of a lab where we review basic computer science
            terms and practice coding. The goal is to help prepare for the first
            quiz of the semester.
"""
import math

def distance(x1, y1, x2, y2):
    squared_distance = (x2-x1)**2 + (y2-y1)**2
    distance = math.sqrt(squared_distance)
    return distance

def compute_triangle_area(side_length):
    """Based on the side length provided, this computes the area of 
    an equilateral triangle with sides of this length.
    Parameter:
        side_length (float):  the side length of the equil. triangle.
    Return:
        area (float): the area of the equilateral triangle.
    """
    return None

def main():
    val1 = input("What is the x-coordinate for the first point?")
    val2 = input("What is the y-coordinate for the first point?")
    val3 = input("What is the x-coordinate for the second point?")
    val4 = input("What is the y-coordinate for the second point?")

    distance(val1, val2, val3, val4)
    compute_triangle_area(distance)

    print("The distance between your points is 10.")
    print("An equilateral triangle with that base has an area of 20.")


if __name__=="__main__":
    main()
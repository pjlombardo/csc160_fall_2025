'''
File:       U1_14_quadratic_formula.py
Author:     P. Lombardo
Date:       ...
Purpose:    A practice task that uses if-statements to implement the quadratic formula.
'''
# import 
import math

# Quadratic formula
def quadratic_formula(a, b, c):
    """This function determines whether there are 0, 1, or 2 solutions to the 
    quadratic equation: a*(x**2) + b*x + c == 0
    
    Parameters:
        a (float): the constant of the squared-term in the quadratic equation
        ...please finish the docstring for this function
    
    Return:
        solution (list):   This may be empty, have one element, or two
                            depending on the value of b^2 - 4*a*c
    """
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        solution_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
        return [solution_1, solution_2]
    elif discriminant < 0:
        # no real solutions
        return []
    else:
        # one real solution
        solution = -b / (2 * a)
        return [solution]
    
def print_result(solution_tuple):
    """ Take a tuple with the solution to a quadratic formula problem
    and print the roots (two, one, or none) in a nice way for the user
    Parameters:
        solution_tuple (tuple):   This will contain the solution as either an
                                    empty tuple, a tuple with one element, or
                                    a tuple with 2 elements.
    Return: None
    Note: we'll print a nice message about the roots.
    """
    # from the solution tuple, we need to branch
    # if the tuple is empty: print no real roots exist
    # else if the tuple has one element, print there is only one root, it is ....
    # else if the tuple has two elemetns, print there are two roots, they are ... and ...
    if len(solution_tuple)==1:
        print(f"There is one solution; it is {solution_tuple[0]}.")
    elif len(solution_tuple) == 0:
        print("There are no real solutions to this quadratic.")
    else:
        root1 = solution_tuple[0]
        root2 = solution_tuple[1]
        print(f"There are two solutions; the first is {root1:.3f}, and " + \
              f"the second is {root2:.3f}.")
    return None


# Main function
def main():
    sol1 = quadratic_formula(1,1,1)
    print_result(sol1)


    sol2 = quadratic_formula(1,2,1)
    print_result(sol2)

    sol3 = quadratic_formula(1,1,-11)
    print_result(sol3)


# main guard
if __name__ == "__main__":
    main()
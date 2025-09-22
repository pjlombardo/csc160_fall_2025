'''
File:       U1_11_cake.py
Author:     P. Lombardo
Date:       ...
Purpose:    A simple program that asks the user for how many slices of cake they want
            and based on the amount the program prints too much or OK.
'''


# Code goes below

def main():
    # get user input, how much cake? (slices)
    slice_count = float(input("How many slices of cake do you want? "))

    # # branching, determine if user wants too much cake
    # if slice_count > 2.5:
    #     print("That's too much cake!")
    # else:
    #     print("OK, I'll go get your cake.")

    # three brnaches
    if slice_count <= 0:
        print("Come on, have some cake!")
    elif slice_count <= 2.5:
        print("OK, I'll get your cake.")
    else:
        print("Too much cake!")

    return 0


# THis "guard" asks, "has the program been run directly?"
# If it has, it runs main.
if __name__=="__main__":
    main()


"""
fill in later based on other examples....

"""

# imports
import random

# functions
def flip_coin(tails_prob):
    """ doc string for you to do..."""
    random_num = random.random()
    if random_num > tails_prob:
        return "tails"
    else:
        return "heads"

# main function
def main():
    # Steps:
    # Assign a random number between 0 and 1 to random_num
    # Branch:
        # if random_num > 0.5
            # return "tails"
        # else:
            # return "heads"

    # # probably not do this in main, make it a function and call it
    # random_num = random.random()
    # if random_num > 0.5:
    #     print("tails")
    # else:
    #     print("heads")

    # like this!
    print(flip_coin(.49))



# main-guard
if __name__ == "__main__":
    main()
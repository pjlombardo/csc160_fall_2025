'''
File:       U1_09_ISBN13.py
Author:     P. Lombardo
Date:       ...
Purpose:    Here we explore a nice application of modular arithmetic (i.e)
            the % operator. We practice working with functions to verify
            a provided ISBN-13 number.
'''

def get_ISBN_sum(ISBN_string):
    """ This function takes an ISBN-13 number as a string and computes the 
    total sum of the digits.
    Parameters:
        ISBN_string (str):  an ISBN-13 number stored as a string
    Return: total (int), the sum of the digits in the ISBN provided.
    """
    total = 0
    round = 0
    check_vals = ISBN_string[:-1]
    for item in check_vals:
        try:
            number = int(item)
            total += (1+2*(round%2))*number
            round +=1
        except:
            pass
    return total

def get_last_ISBN_digit(ISBN_string):
    """ This function extracts the last digit from a ISBN-13 number stored as a
    string
    Parameters:
        ISBN_string (str): an ISBN-13 number stored as a string
    Return: (int) the last digit of the ISBN-13 number stored as an integer
    """
    return int(ISBN_string[-1])

def verify_ISBN(ISBN_string):
    """Take in a ISBN_string and this will print two things
        1.  (10 - (IBSN_sum mod 10)) mod 10
        2.  last ISBN digit
    Parmeters: ISBN_string (str),  a string version of your ISBN-13 number.
    Return: None
    """
    ISBN_sum = get_ISBN_sum(ISBN_string)
    check_number = (10 - (ISBN_sum % 10)) % 10
    print(check_number)

    last_digit = get_last_ISBN_digit(ISBN_string)
    print(last_digit)
    return None
    

def main():
    # Ask the user for an ISBN-13 number
    # verify it
    # that's all folks.
    ISBN_string = input("What is your ISBN number? ")
    verify_ISBN(ISBN_string)

if __name__=="__main__":
    main()
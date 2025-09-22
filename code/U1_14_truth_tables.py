'''
File:       U1_13_truth_tables.py
Author:     P. Lombardo
Date:       ...
Purpose:    Here is some space to explore NOT, AND, OR, and more complicated 
            boolean expressions.  
            Note: This is an ugly program and not up to standards.  But, it's quick
            to do some exploration.
'''

####################################
## Leave below untouched please ####
###################################
two_bool_possibilities = [(0,0), (0,1), (1,0),(1,1)]
three_bool_possibilities = [(0,0,0), (0,0,1), (0,1,0),(0,1,1),
                            (1,0,0), (1,0,1), (1,1,0), (1,1,1)]

def print_two_bool_truth_table(two_bool_expression_fxn):
    print(f'  p  |  q  | expression')
    print('--------------------')
    for p,q in two_bool_possibilities:
        # make your changes to expression
        expression = two_bool_expression_fxn(p,q)
        print(
            f'  {p}  |  {q}  | {int(expression)}'
        )

def print_three_bool_truth_table(three_bool_expression_fxn):
    print(f'  p  |  q  |  r  | expression')
    print('--------------------')
    for p,q,r in three_bool_possibilities:
        # make your changes to expression
        expression = three_bool_expression_fxn(p,q,r)
        print(
            f'  {p}  |  {q}  |  {r}  | {int(expression)}'
        )

###################################
## Leave above untouched please ####
###################################

###########################
## You may edit below! ####
##########################

# Modify the return statements below with your 
# boolean expressions, or create your own function
def two_bool_expression_fxn(p,q):
    return p and q

def three_bool_expression_fxn(p,q,r):
    
    return p and (q or r)


def three_bool_expr2(p,q,r):
    return not (not p or (not q and not r))

# We use these functions as the arguments to the 
# print_***_bool_truth_table() functions.

def main():
    print_two_bool_truth_table(two_bool_expression_fxn)
    print()
    print_three_bool_truth_table(three_bool_expression_fxn)
    print()
    print_three_bool_truth_table(three_bool_expr2)

if __name__=="__main__":
    main()



# def main():
#     MAIN_VAR = 10
#     def test_fxn(num):
#         return num*MAIN_VAR
    
#     print(test_fxn(3))

# main()

def test_fxn(num):
    return num*MAIN_VAR

def main():
    global MAIN_VAR
    MAIN_VAR = 10
    print(test_fxn(3))

main()
'''
File:       U1_01_example_program.py
Author:     P. Lombardo
Date:       ...
Purpose:    This is an example program to provide a sense of what you'll be making
            by the end of the course.  It is not important that you understand any
            of this now!
'''

HW_WEIGHT = .2
QUIZ_WEIGHT = .55
FINAL_WEIGHT = .25

weights = (HW_WEIGHT, QUIZ_WEIGHT, FINAL_WEIGHT)

kinds = ('homework','quiz','final exam')

def get_grade(kind):
    if kind != "final exam":
        val = int(input(f"What is your {kind} average: "))
        print("")
    else:
        val = int(input(f"What is your {kind} score: "))
        print("")
    return val

def gather_grades():
    grades = []
    for kind in kinds:
        val = get_grade(kind)
        grades.append(val)
    return grades

def compute_weighted_average(grade_list):
    course_score = 0
    for i in range(3):
        course_score += weights[i]*grade_list[i]
    return course_score

def main():
    print("\nWelcome to our weighted-average calculator.\nThis calculator is based on the following weights: homeworks are worth 20%, quizzes are worth 55%, and the final exam is worth 25%.\nPlease enter your grade or average grade for each category now.\n")
    
    grades = gather_grades()

    course_grade = compute_weighted_average(grades)

    print(f"Your course scores is {course_grade:.3f}")

    if course_grade <60:
        print("\nSo sorry, you have failed the course. Better luck next time!")
    else:
        print("\nCongratulations, you have passed the course!")


if __name__=="__main__":
    main()




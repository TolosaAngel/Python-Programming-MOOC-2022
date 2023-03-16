from math import floor

list_exam_points = []
list_exercise_points = []
list_of_sum_of_points = []

def grade_distribution():
    grade_zero = "0: "
    grade_one = "1: "
    grade_two = "2: "
    grade_three = "3: "
    grade_four = "4: "
    grade_five = "5: "

    for i in range(len(list_of_sum_of_points)):
        if list_exam_points[i]<10:
            grade_zero+="*"
        elif list_of_sum_of_points[i]>=28:
            grade_five+="*"
        elif 24<=list_of_sum_of_points[i]<=27:
            grade_four+="*"
        elif 21<=list_of_sum_of_points[i]<=23:
            grade_three+="*"
        elif 18<=list_of_sum_of_points[i]<=20:
            grade_two+="*"
        elif 15<=list_of_sum_of_points[i]<=17:
            grade_one+="*"
        else:
            grade_zero+="*"

    print(grade_five)
    print(grade_four)
    print(grade_three)
    print(grade_two)
    print(grade_one)
    print(grade_zero)        

def pass_percentage():
    total_pass = 0

    for i in range(len(list_of_sum_of_points)):
        if list_exam_points[i]>=10 and list_of_sum_of_points[i]>14:
            total_pass+=1
    
    pass_percentage = float(total_pass/len(list_of_sum_of_points))*100

    return f"{pass_percentage:.1f}"


def points_average():
    result = sum(list_of_sum_of_points)/len(list_exam_points)

    return f"{result:.1f}"

def show_statistics():
    print("Statistics:")
    print(f"Points average: {points_average()}")
    print(f"Pass percentage: {pass_percentage()}")
    print("Grade distribution:")
    grade_distribution()

def sum_of_points():
    for i in range(len(list_exam_points)):
        list_of_sum_of_points.append(list_exam_points[i] + list_exercise_points[i])

def to_exercise_points(exercices):
    number = floor(exercices*0.10)
    return number

def check_input(user_input):
    split = user_input.split()

    if len(split)==0:
        return False
    else:
        list_exam_points.append(int(split[0]))
        list_exercise_points.append( to_exercise_points(int(split[1])) )

        return True

def data_input():
    validator = True

    while validator:
        user_input = input("Exam points and exercises completed: ")

        validator = check_input(user_input)


def main():
    data_input()
    sum_of_points()
    show_statistics()

main()
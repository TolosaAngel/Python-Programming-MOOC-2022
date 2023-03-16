def average(students: dict, name):
    sum_grades = 0
    
    for i in range(len(students[name])):
        sum_grades += students[name][i][1]

    return sum_grades/len(students[name])

def add_student(students: dict, name):
    if name not in students:
        students[name]=[]

def print_student(students: dict, name):
    if name in students:
        print(f"{name}:")

        if students[name]==[]:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")

            for i in range(len(students[name])):
                print(f"  {students[name][i][0]} {students[name][i][1]}")

            print(f" average grade {average(students, name)}")
    else:
        print(f"{name}: no such person in the database")

def add_course(students: dict, name, my_list: list):
    dir = 0
    mark = False
    course, grade = my_list

    if name in students and grade!=0:
        for i in range(len(students[name])):
            if course in students[name][i]:
                dir = i
                mark = True
                break

        if mark:
            if grade>students[name][dir][1]:
                students[name].pop(dir)
                students[name].append( (course,grade) )
        else:
            students[name].append( (course,grade) )

def summary(students: dict):
    print(f"students {len(students)}")

    most_courses_number = 0
    most_courses_name = ""
    best_average_number = 0
    best_average_name = ""
    
    for name in students:
        if len(students[name])>=most_courses_number:
            most_courses_number = len(students[name])
            most_courses_name = name

        if average(students, name)>= best_average_number:
            best_average_number = average(students, name)
            best_average_name = name

    print(f"most courses completed {most_courses_number} {most_courses_name}")   
    print(f"best average grade {best_average_number} {best_average_name}")   

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")

    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")

    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
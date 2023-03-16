student_file = input("Student information: ").strip()
exercises_file = input("Exercises completed: ").strip()
exam_file = input("Exam points: ").strip()

students_dictionary = {}

with open(student_file) as students_info:
    for line in students_info:
        data = line.split(";")

        if data[0] == "id":
            continue

        students_dictionary[data[0]] = (data[1] + " " + data[2]).strip()

exercises_dictionary = {}

with open(exercises_file) as exercises_info:
    for line in exercises_info:
        data = line.split(";")

        if data[0] == "id":
            continue

        sum_of_exercises = 0

        for i in range(1,len(data)):
            sum_of_exercises += int(data[i])

        exercises_dictionary[data[0]] = sum_of_exercises

exam_dictionary = {}

with open(exam_file) as exam_info:
    for line in exam_info:
        data = line.split(";")

        if data[0] == "id":
            continue

        sum_of_points = 0

        for i in range(1,len(data)):
            sum_of_points += int(data[i])

        exam_dictionary[data[0]] = sum_of_points

for student_id in students_dictionary:
    total_points = (exercises_dictionary[student_id]*10)//40 + exam_dictionary[student_id]
    grade = 0

    if total_points >= 28:
        grade = 5
    elif 24<=total_points<=27:
        grade = 4
    elif 21<=total_points<=23:
        grade = 3
    elif 18<=total_points<=20:
        grade = 2
    elif 15<=total_points<=17:
        grade = 1
    else:
        grade = 0

    print(f"{students_dictionary[student_id]} {grade}")
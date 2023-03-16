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

header = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
print(f"{header[0]:<30}{header[1]:<10}{header[2]:<10}{header[3]:<10}{header[4]:<10}{header[5]:<10}")

for student_id in students_dictionary:
    exec_pts = (exercises_dictionary[student_id]*10)//40
    tot_pts = exec_pts + exam_dictionary[student_id]
    grade = 0

    if tot_pts >= 28:
        grade = 5
    elif 24<=tot_pts<=27:
        grade = 4
    elif 21<=tot_pts<=23:
        grade = 3
    elif 18<=tot_pts<=20:
        grade = 2
    elif 15<=tot_pts<=17:
        grade = 1
    else:
        grade = 0
    
    print(f"{students_dictionary[student_id]:<30}{exercises_dictionary[student_id]:<10}{exec_pts:<10}{exam_dictionary[student_id]:<10}{tot_pts:<10}{grade:<10}")
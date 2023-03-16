name_file1 = input("Student information: ").strip()
name_file2 = input("Exercises completed: ").strip()

students_dictionary = {}

with open(name_file1) as students_info:
    for line in students_info:
        data = line.split(";")

        if data[0] == "id":
            continue

        students_dictionary[data[0]] = (data[1] + " " + data[2]).strip()

exercises_dictionary = {}

with open(name_file2) as exercises_info:
    for line in exercises_info:
        data = line.split(";")

        if data[0] == "id":
            continue

        sum_of_exercises = 0

        for i in range(1,len(data)):
            sum_of_exercises += int(data[i])

        exercises_dictionary[data[0]] = sum_of_exercises

final_dictionary = {}

for stu_id in students_dictionary:
    for exe_id in exercises_dictionary:
        if stu_id==exe_id:
            final_dictionary[students_dictionary[stu_id]] = exercises_dictionary[exe_id]
            break

for student in final_dictionary:
    print(f"{student} {final_dictionary[student]}")
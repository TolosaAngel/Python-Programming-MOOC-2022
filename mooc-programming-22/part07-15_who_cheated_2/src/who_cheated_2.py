from csv import *
from datetime import *

def students_start_times():
    students_start_times = {}

    with open("start_times.csv") as start_times:
        for student in reader(start_times, delimiter=";"):
            hour = student[1].split(":")
            start_time = timedelta(hours=int(hour[0]), minutes=int(hour[1]))

            students_start_times[student[0]] = start_time

    return students_start_times

def students_submissions(students_start_times: dict):
    students = {}

    with open("submissions.csv") as submissions:
        for submission in reader(submissions, delimiter=";"):
            student = submission[0]
            exercise = int(submission[1])
            grade = int(submission[2])
            
            hour = submission[3].split(":")
            submission_time = timedelta(hours=int(hour[0]), minutes=int(hour[1]))
            time_difference = submission_time - students_start_times[student] 

            if timedelta(hours=0)<=time_difference<=timedelta(hours=3):
                if student in students:
                    if grade>=students[student][exercise-1]:
                        students[student][exercise-1] = grade
                else:
                    my_list = [0, 0, 0, 0, 0, 0, 0, 0]
                    students[student] = my_list
                    students[student][exercise-1] = grade

    return students
    
def final_points():
    start_times = students_start_times()
    submissions = students_submissions(start_times)

    final_dict = {}

    for student in submissions:
        final_dict[student] = sum(submissions[student])

    return final_dict
    
if __name__ == "__main__":
    print(final_points())
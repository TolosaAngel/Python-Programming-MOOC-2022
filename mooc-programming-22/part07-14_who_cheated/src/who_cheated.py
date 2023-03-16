from csv import *
from datetime import *

def cheaters():
    students = {}
    cheaters = []

    with open("start_times.csv") as start_times:
        for student in reader(start_times, delimiter=";"):
            hour = student[1].split(":")
            start_time = timedelta(hours=int(hour[0]), minutes=int(hour[1]))

            students[student[0]] = start_time
            
    with open("submissions.csv") as submissions:
        for student in reader(submissions, delimiter=";"):
            hour = student[3].split(":")
            sub_time = timedelta(hours=int(hour[0]), minutes=int(hour[1]))

            if sub_time>students[student[0]]+timedelta(hours=3):
                if student[0] not in cheaters:
                    cheaters.append(student[0])

    return cheaters

if __name__ == "__main__":
    print(cheaters())
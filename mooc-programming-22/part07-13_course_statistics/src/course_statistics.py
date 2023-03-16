import urllib.request
from math import *
from json import *

def retrieve_all():
    courses = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    data = courses.read()
    list_of_data = loads(data)

    final_list = []

    for course in list_of_data:
        if course["enabled"]:
            full_name = course["fullName"]
            name = course["name"]
            year = course["year"]
            exercises = sum(course["exercises"])

            my_tuple = full_name, name, year, exercises

            final_list.append(my_tuple)

    return final_list

def retrieve_course(course_name: str):
    course_data = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")

    specific_data = course_data.read()
    list_specific_data = loads(specific_data)

    final_dictionary = {}

    students = 0
    hours = 0
    exercises = 0

    for week in list_specific_data:
        students = max(int(list_specific_data[week]["students"]),students)
        hours += int(list_specific_data[week]["hour_total"])
        exercises += int(list_specific_data[week]["exercise_total"])

    final_dictionary["weeks"] = len(list_specific_data)
    final_dictionary["students"] = students
    final_dictionary["hours"] = hours
    final_dictionary["hours_average"] = floor(hours/students)
    final_dictionary["exercises"] = exercises
    final_dictionary["exercises_average"] = floor(exercises/students)

    return final_dictionary

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))
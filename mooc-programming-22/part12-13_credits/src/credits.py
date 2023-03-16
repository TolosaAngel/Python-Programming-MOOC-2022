from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(course_attemps: list):
    return reduce(lambda total_sum, attemp: total_sum + attemp.credits, course_attemps, 0)

def filter_grade(course_attemps: list, grade: int):
    return list(filter(lambda attemp: attemp.grade>=grade , course_attemps))

def sum_of_passed_credits(course_attemps: list):
    return reduce(lambda total_sum, attemp: total_sum + attemp.credits, filter_grade(course_attemps, 1), 0)

def average(course_attemps: list):
    filter_list = filter_grade(course_attemps, 1)
    return reduce(lambda total_sum, attemp: total_sum + attemp.grade, filter_list, 0) / len(filter_list)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
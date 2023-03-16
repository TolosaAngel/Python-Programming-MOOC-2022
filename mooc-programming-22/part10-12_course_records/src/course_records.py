class Course:
    def __init__(self, course: str, grade: int, credits: int):
        self.__course = course
        self.__grade = grade
        self.__credits = credits

    @property
    def course(self):
        return self.__course 
    
    @property
    def grade(self):
        return self.__grade 
    
    @property
    def credits(self):
        return self.__credits 

    def __str__(self):
        return f"{self.__course} ({self.__credits} cr) grade {self.__grade}"

class CourseRecordsApplication:
    def __init__(self):
        self.__courses = {}

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")

        if course in self.__courses:
            if grade>self.__courses[course].grade:
                self.__courses[course] = Course(course,grade,credits)
        else:
            self.__courses[course] = Course(course,grade,credits)

    def get_course_data(self):
        course = input("course: ")
        
        if course in self.__courses:
            print(self.__courses[course])
        else:
            print("no entry for this course")

    def statistics(self):
        completed_courses = len(self.__courses)
        total_credits = 0
        grades = {"1":0, "2":0, "3":0, "4":0, "5":0}

        for course in self.__courses:
            total_credits += int(self.__courses[course].credits)
            key = self.__courses[course].grade
            grades[key] += 1

        mean = (grades["1"] + grades["2"]*2 + grades["3"]*3 + grades["4"]*4 + grades["5"]*5) / completed_courses

        print(f"{completed_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")

        for iterator in range(5,0,-1):
            draw = 'x' * grades[str(iterator)]
            print(f"{iterator}: {draw}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()

application = CourseRecordsApplication()
application.execute()
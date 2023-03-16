class Question:
    def __init__(self, question: str, maximum_points: int):
        self.__question = question
        self.__maximum_points = maximum_points

    @property
    def question(self):
        return self.__question
    
    @question.setter
    def question(self, question: str):
        self.__question = question
    
    @property
    def maximum_points(self):
        return self.__maximum_points
    
    @maximum_points.setter
    def maximum_points(self, maximum_points: int):
        self.__maximum_points = maximum_points
    
    def __str__(self):
        return f"{self.__question}, {self.__maximum_points} points"
    
class Exam:
    def __init__(self, subject: str, date: str):
        self.subject = subject
        self.date = date
        self.exam_questions = []

    def add_question(self, question: Question):
        self.exam_questions.append(question)

    def print_questions(self):
        print(f"Exam on {self.subject}, questions:")

        for question in self.exam_questions:
            print(question)

    def total_points(self):
        points = 0

        for question in self.exam_questions:
            points += question.maximum_points

        return points
    
if __name__ == "__main__":
    q1 = Question("When was the Olympics held in Helsinki", 10)
    q2 = Question("when did Finland become independent", 5)

    print(q1)

    exam = Exam("History", "1.12.2021")
    exam.add_question(q1)
    exam.add_question(q2)

    exam.print_questions()
    print("Maximum points of the exam:", exam.total_points())
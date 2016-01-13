# You are given two classes, Student and Grade, where Student is the base class and Grade is the derived class.
# Completed code for Student and stub code for Grade are provided. Complete the code for Grade class.
class Student:
    def __init__(self, first_name, last_name, phone):
        self.firstName = first_name
        self.lastName = last_name
        self.phone = phone

    def display(self):
        print("First Name:", self.firstName)
        print("Last Name:", self.lastName)
        print("Phone:", self.phone)


class Grade(Student):
    def __init__(self, first_name, last_name, phone, score):
        super().__init__(first_name, last_name, phone)
        self.score = score

    def calculate(self):
        if self.score < 40:
            return 'D'
        elif 40 <= self.score < 60:
            return 'B'
        elif 60 <= self.score < 75:
            return 'A'
        elif 75 <= self.score < 90:
            return 'E'
        elif 60 <= self.score <= 100:
            return 'O'


stu = Grade(input().strip(), input().strip(), int(input()), int(input()))
stu.display()
print("Grade:", stu.calculate())

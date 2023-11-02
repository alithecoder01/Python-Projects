from Student import Student

class MsStudent(Student):
    def __init__(self, name, id, major, gpa):
        super().__init__(name, id, major, gpa)
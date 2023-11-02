from Student import Student

class BsStudent(Student):
    def __init__(self, name, id, major, gpa):
        super().__init__(name, id, major, gpa)

    
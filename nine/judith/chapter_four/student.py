class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def set_student_name_mark(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks


judith = Student("Joy", 34)
print('The initial name is', judith.student_name, 'and mark is', judith.marks)
judith.marks = 49
judith.student_name = "Baby"
print('The updated name is', judith.student_name, 'and mark is', judith.marks)


class StudentAgain:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name


student_data = StudentAgain(2, "femi")
print(student_data.__dict__)
student_data.__setattr__("student_class", "cohort 8")
print(student_data.__dict__)
student_data.__delattr__("student_name")
print(student_data.__dict__)



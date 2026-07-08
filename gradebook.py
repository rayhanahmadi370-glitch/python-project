class Gradebook:
    def __init__(self):
        self.__students = []
        self.__courses = []

def add_student(self, student):
    self.__students.append(student)
    print("Student added.")

def remove_student(self, student_id):
    for student in self.__students:
        if student.get_student_id() == student_id:
            self.__students.remove(student)
            print("Student removed.")
            return

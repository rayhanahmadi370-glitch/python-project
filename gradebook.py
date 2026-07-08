class Gradebook:
    def __init__(self):
        self.__students = []
        self.__courses = []

    # Student Methods

# add student
    def add_student(self, student):
        for s in self.__students:
            if s.get_student_id() == student.get_student_id():
                print("Student ID already exists.")
                return

        self.__students.append(student)
        print("Student added successfully.")

#remove student
    def remove_student(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                self.__students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found.")

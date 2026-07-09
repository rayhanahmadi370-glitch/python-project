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

    def find_student(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                return student
        return None

    def display_all_students(self):
        if len(self.__students) == 0:
            print("No students found.")
            return

        for student in self.__students:
            student.display_info()
            print("-" * 30)

    def find_student(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                return student
        return None

    def display_all_students(self):
        if len(self.__students) == 0:
            print("No students found.")
            return

        for student in self.__students:
            student.display_info()
            print("-" * 30)


    # Course Methods
    def add_course(self, course):
        for c in self.__courses:
            if c.get_course_code() == course.get_course_code():
                print("Course code already exists.")
                return

        self.__courses.append(course)
        print("Course added successfully.")

    def find_course(self, course_code):
        for course in self.__courses:
            if course.get_course_code() == course_code:
                return course
        return None

    def display_all_courses(self):
        if len(self.__courses) == 0:
            print("No courses available.")
            return

        for course in self.__courses:
            course.display_course()
            print("-" * 30)

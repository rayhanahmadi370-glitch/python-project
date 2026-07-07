from person import Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__courses = {}

    # Getter
    def get_student_id(self):
        return self.__student_id

    # Setter
    def set_student_id(self, student_id):
        self.__student_id = student_id

 # Enroll in a course
    def enroll_course(self, course_name):
        if course_name not in self.__courses:
            self.__courses[course_name] = None
            print(f"Enrolled in {course_name}.")
        else:
            print("Student is already enrolled in this course.")


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

    # Remove a course
    def remove_course(self, course_name):
        if course_name in self.__courses:
            del self.__courses[course_name]
            print(f"Removed {course_name}.")
        else:
            print("Course not found.")

  # Add or update a grade
    def add_grade(self, course_name, grade):
        if course_name in self.__courses:
            if 0 <= grade <= 100:
                self.__courses[course_name] = grade
                print("Grade added successfully.")
            else:
                print("Grade must be between 0 and 100.")
        else:
            print("Student is not enrolled in this course.")

 # Calculate average grade
    def calculate_average(self):
        grades = []

        for grade in self.__courses.values():
            if grade is not None:
                grades.append(grade)

        if len(grades) == 0:
            return 0

        return sum(grades) / len(grades)

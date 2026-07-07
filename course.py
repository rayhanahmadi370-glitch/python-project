class Course:
    def __init__(self, course_name, course_code, instructor):
        self.__course_name = course_name
        self.__course_code = course_code
        self.__instructor = instructor

    # Getters
    def get_course_name(self):
        return self.__course_name

    def get_course_code(self):
        return self.__course_code

    def get_instructor(self):
        return self.__instructor

    # Setters
    def set_course_name(self, course_name):
        self.__course_name = course_name

    def set_course_code(self, course_code):
        self.__course_code = course_code

    def set_instructor(self, instructor):
        self.__instructor = instructor

    # Display course information
    def display_course(self):
        print("\n===== Course Information =====")
        print(f"Course Name : {self.__course_name}")
        print(f"Course Code : {self.__course_code}")
        print(f"Instructor  : {self.__instructor}")

    # String representation
    def __str__(self):
        return f"{self.__course_code} - {self.__course_name}"

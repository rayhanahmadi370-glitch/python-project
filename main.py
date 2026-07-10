from gradebook import Gradebook
from student import Student
from course import Course

def get_text(message):
    while True:
        text = input(message).strip()

        if text != "":
            return text

        print("Input cannot be empty. Please try again.")
def get_age():
    while True:
        try:
            age = int(input("Enter student age: "))

            if age > 0:
                return age

            print("Age must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")
def get_grade():
    while True:
        try:
            grade = float(input("Enter grade (0-100): "))

            if 0 <= grade <= 100:
                return grade

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    gradebook = Gradebook()

    while True:
        print("\n" + "=" * 40)
        print("STUDENT GRADEBOOK & COURSE MANAGER")
        print("=" * 40)
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. Add Course")
        print("5. View All Courses")
        print("6. Enroll Student in Course")
        print("7. Assign Grade")
        print("8. Student Report")
        print("9. Show All Reports")
        print("10. Show Top Student")
        print("11. Show Class Average")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = get_text("Enter student name: ")
            age = get_age()
            student_id = get_text("Enter student ID: ")

            student = Student(name, age, student_id)
            gradebook.add_student(student)

        elif choice == "2":
            student_id = get_text("Enter student ID: ")
            gradebook.remove_student(student_id)

        elif choice == "3":
            gradebook.display_all_students()

        elif choice == "4":
            course_name = get_text("Enter course name: ")
            course_code = get_text("Enter course code: ")
            instructor = get_text("Enter instructor name: ")

            course = Course(course_name, course_code, instructor)
            gradebook.add_course(course)

        elif choice == "5":
            gradebook.display_all_courses()

        elif choice == "6":
            student_id = get_text("Enter student ID: ")
            course_code = get_text("Enter course code: ")

            gradebook.enroll_student(student_id, course_code)

        elif choice == "7":
            student_id = get_text("Enter student ID: ")
            course_code = get_text("Enter course code: ")
            grade = get_grade()

            gradebook.assign_grade(student_id, course_code, grade)

        elif choice == "8":
            student_id = get_text("Enter student ID: ")
            gradebook.show_student_report(student_id)

        elif choice == "9":
            gradebook.show_all_reports()

        elif choice == "10":
            gradebook.display_top_student()

        elif choice == "11":
            gradebook.class_average()

        elif choice == "0":
            print("Thank you for using Student Gradebook & Course Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

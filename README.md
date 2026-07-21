Student Gradebook & Course Manager

Overview

Student Gradebook & Course Manager is a terminal-based Python application developed as a final project for an introductory Python programming course. The application allows users to manage students, courses, enrollments, and grades through a simple menu-driven interface.

The project demonstrates the use of core Python programming concepts, including Object-Oriented Programming (OOP), functions, lists, dictionaries, encapsulation, inheritance, and method overriding.

---

Features

- Add new students
- Remove students
- View all students
- Add new courses
- View all courses
- Enroll students in courses
- Assign grades to students
- Generate individual student reports
- Display reports for all students
- Calculate the class average
- Display the top-performing student
- Search students by ID
- Count the total number of students
- Count the total number of courses
- Input validation for user entries

---

Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Terminal/Console Interface

No external libraries or third-party packages were used.

---

Project Structure

student-gradebook/

├── person.py
├── student.py
├── course.py
├── gradebook.py
├── main.py
└── README.md

---

Object-Oriented Design

Person

The parent class that stores common information such as a person's name and age.

Student

Inherits from the "Person" class and manages student IDs, enrolled courses, grades, and academic reports.

Course

Represents a course with its name, course code, and instructor.

Gradebook

Acts as the manager of the application by handling students, courses, enrollment, grade assignment, reports, and statistics.

---

Python Concepts Demonstrated

- Classes and Objects
- Encapsulation
- Inheritance
- Method Overriding
- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Input Validation

---

How to Run

1. Clone this repository.

2. Navigate to the project folder.

3. Run the application:

python main.py

---

Sample Menu

1. Add Student
2. Remove Student
3. View All Students
4. Add Course
5. View All Courses
6. Enroll Student in Course
7. Assign Grade
8. Student Report
9. Show All Reports
10. Show Top Student
11. Show Class Average
12. Search Student by ID
13. Count Total Students
14. Count Total Courses
0. Exit

---

Future Improvements

- Save and load data using files or a database.
- Student login system.
- Graphical User Interface (GUI).
- Search students by name.
- GPA calculation.
- Export reports.

---

Author

Reyhaneh Ahmadi 

Final Python Project – Student Gradebook & Course Manager

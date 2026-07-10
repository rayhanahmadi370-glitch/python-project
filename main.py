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

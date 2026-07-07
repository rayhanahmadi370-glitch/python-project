class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

     # Getters
        def get_name(self):
            return self.__name

        def get_age(self):
            return self.__age
 # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")


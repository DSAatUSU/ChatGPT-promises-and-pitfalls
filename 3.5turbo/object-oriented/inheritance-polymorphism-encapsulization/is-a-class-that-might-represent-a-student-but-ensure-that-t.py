class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        self.__grade = new_grade


# Test the class
student = Student('John', 18, 'A')
print(student.get_name())  # Output: John
print(student.get_age())  # Output: 18
print(student.get_grade())  # Output: A

student.set_grade('B')
print(student.get_grade())  # Output: B

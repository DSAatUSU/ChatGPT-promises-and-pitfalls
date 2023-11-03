class Student:
    def __init__(self, name, age, school, grade):
        self._name = name
        self._age = age
        self._school = school
        self._grade = grade

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_school(self):
        return self._school

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

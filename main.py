
class Person:
    def __init__(self):
        pass

class Student(Person):
    def __init__(self):
        self.name = "N/A"
        self.age = 19
        self.height = 207
        self.school = 98

    def vivod(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Рост: {self.height}")
        print(f"Школа: {self.school}")


student = Student()

student.vivod()

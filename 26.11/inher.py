
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hour):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hour = num_of_hour

    def show_finance(self):
        return self.rate * self.num_of_hour


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship


if __name__ == "__main__":
    print("Starting")
    p1 = Person("Nemo", 69)
    print(p1)
    print(f"{Person.__mro__ = }")
    print(f"{Employee.__mro__ = }")
    print(f"{Student.__mro__ = }")
    print(f"{WorkingStudent.__mro__ = }")
    os4 = WorkingStudent(name="Mati", age=19, rate=7, num_of_hour=168, scholarship=100)
    os5 = WorkingStudent(name="Teet", age=21, rate=16, num_of_hour=168, scholarship=500)
    print(os4)
    print(os5)

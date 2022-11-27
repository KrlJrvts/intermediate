from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r.area())
    print(r.circuit())

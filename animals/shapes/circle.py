from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return 3.14 * self._radius * self._radius
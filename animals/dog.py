from .animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def make_sound(self):
        return "Woof!"
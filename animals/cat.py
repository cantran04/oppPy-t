from .animal import Animal

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def make_sound(self):
        return "Meow!"
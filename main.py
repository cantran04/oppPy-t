# main.py
from animals.animal import Animal
from animals.dog import Dog
from animals.cat import Cat
from animals.shapes.circle import Circle

animal = Animal("Generic Animal", 5)
print("Animal:", animal.get_name(), "Age:", animal.get_age())

dog = Dog("Buddy", 3, "Golden Retriever")
print("Dog:", dog.get_name(), "Age:", dog.get_age(), "Breed:", dog.get_breed())
print("Dog Sound:", dog.make_sound())

cat = Cat("Whiskers", 2, "Gray")
print("Cat:", cat.get_name(), "Age:", cat.get_age(), "Color:", cat.get_color())
print("Cat Sound:", cat.make_sound())

circle = Circle(5)
print("Circle Area:", circle.calculate_area())

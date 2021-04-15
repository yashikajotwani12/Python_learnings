class Animals:
    animaltype="mammal"
class Pets(Animals):
    type="white"
class Dog(Pets):
    @staticmethod
    def bark():
     print("bark")

dog=Dog()
dog.bark()
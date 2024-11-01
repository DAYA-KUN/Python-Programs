class Animal:
    def speak(self):
        return "Animal speaks"

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        return "Meow!"

my_cat = Cat()
print(my_cat.speak()) 
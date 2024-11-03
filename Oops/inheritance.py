class Animal:
    def speak(self):
        return "Animal speaks"

class Cat(Animal):  # Cat inherits from Animal

    # def __init__(self,name):
    #     self.name=name

    def speak(self,name):
        self.name=name
        return f"{self.name} says Meow!" # Method Overriding

my_cat = Cat()
print(my_cat.speak("Meowz")) 
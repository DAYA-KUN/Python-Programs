#Write a Car class with attributes like make, model, and year. Include a method display_info() to print out the car's details.

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"The make is {self.make}. The model is {self.model}. It was made in the year {self.year}")

car1=Car("Electric","Tesla",2019)
car1.display_info()
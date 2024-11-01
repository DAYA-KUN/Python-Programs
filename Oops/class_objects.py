class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_details(self):
        print(f"The name of the student is {self.name}, The age of the student is {self.age}.")


student1=Student("Daya",18)
student1.print_details()
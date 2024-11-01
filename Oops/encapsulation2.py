class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public attribute
        self._department = "HR"    # Protected attribute
        self.__salary = salary     # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

emp1=Employee("Daya",50000)
print(emp1.get_salary())#Salary can be accessed only with  a public method

print(emp1._department) #department can be accessed directly as it is a protected variable
print(emp1.name) #name can be accessed directly as it is a public variable

print(emp1.__salary) #Cannot directly print salary as it is a private variable
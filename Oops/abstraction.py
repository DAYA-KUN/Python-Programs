from abc import ABC,abstractmethod # Abstract Base Classes

class Shape(ABC):
    @abstractmethod #Python Decorator - Function
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def area(self):
        return f"The Area of Rectangle is {self.width*self.height}"
    
rect=Rectangle(20,30)
print(rect.area())

#Hide uncessary details.
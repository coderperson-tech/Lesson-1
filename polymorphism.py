print("polymorphism in OOPs")

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    

circle = Circle(5)
square = Square(4)

print("Area of a circle: ", circle.area())

print("Area of square:", square.area())


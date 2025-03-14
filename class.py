class Car:
    def __init__(self, name, brand, color):    #constructor(special function for intilizizing values)
        self.name =name
        self.brand = brand
        self.color = color
    

    def display(self):
      print("This car is a ", {self.name}, {self.brand}, {self.color})

#Object creation

car1 = Car("james", "toyota", "red")
car2 = Car("bob","lexus", "pink" )

car1.display()
car2.display()
class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def show_details(self):
        print(f"Fruit: {self.name}, Color: {self.color}")
    def __del__(self):
        print(f"{self.name} has been deleted")


apple = fruit("apple", "red")
apple.show_details()
banana = fruit("banana", "yellow")
banana.show_details()
del banana


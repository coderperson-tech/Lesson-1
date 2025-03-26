print("Encapsulation in OOPS")

class Square():
    def __init__(self):
        self.__side = 10
    
    def area(self):
        print("Side:", self.__side)
        print("Area:", self.__side ** 2)
    

sq = Square()
sq.area()

sq.__side = 20
sq.area()
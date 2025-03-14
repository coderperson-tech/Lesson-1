class Student:
    schoolname = "greenwood highschool"
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def show(self):
        print(f"students:", {self.name}, "grade:", {self.grade}, "highschool:", {Student.schoolname})


student1 = Student("Alice", 10)
student2 = Student("BoB", 12)

student1.show()
student2.show()
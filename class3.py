class Employee:
    company_name  = "TechCorp"
    total_employee = 0 
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    
        Employee.total_employee += 1
    
    def show_details(self):
        print(f"Employee", {self.name}, "salary:", {self.salary})

    
    def show_total_employess():
        print(f"total employee at {Employee.company_name}: {Employee.total_employee}")




employee1 = Employee("jack", 500000)
employee2 = Employee("bob", 400000)
employee3 = Employee("chase", 200000)

employee1.show_details()
employee2.show_details()
employee3.show_details()

Employee.show_total_employess()
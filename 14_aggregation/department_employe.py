# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee: {self.name}"

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def show_employee(self):
        return f"Department: {self.name}, {self.employee.get_details()}"
    
employee = Employee("Ali")
department = Department("Engineering", employee) 
print(department.show_employee())   

print(employee.get_details())

    
class Employee:
    def __init__(self,name,salary: float):
        self.name=name
        self.salary=salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name,salary)
        self.department=department

    def get_details(self):
        bonus = self.get_bonus() - self.salary
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}, Bonus: {bonus}"
    
    def get_bonus(self):
        bonus=self.salary * 0.2
        total=self.salary+bonus
        return total
    
class Developer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name,salary)
        self.language=language

    def get_details(self):
        bonus = self.get_bonus() - self.salary
        return f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}, Bonus: {bonus}"
    
    def get_bonus(self):
        bonus=self.salary * 0.1
        total=self.salary+bonus
        return total
    
def display_all(person):
    for i in person:
        print(i.get_details())

e1=[Manager("Lovenesh",3000,"HR"),
Developer("Aditya",1000,"Python")]
display_all(e1)
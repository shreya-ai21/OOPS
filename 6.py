class Employee():
    def __init__(self, name:str, age:int, salary:float):
        self.name=name
        self.age=age
        self.salary=salary
        
emp1=Employee('Shreya','20',6400000.45)
print(emp1.name,emp1.age,emp1.salary)
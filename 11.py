class Employee():
    def __init__(self, name:str, age:int,salary:float):
        self.name=name
        self.age=age
        self.__salary=salary
        self.work()
        self.show()
    
    def work(self):
        print('Working')
    
    def show(self):
        print(f"Name:{self.name}\nAge:{self.age}\nSalary:{self.__salary}")

emp1=Employee('Shreya','20',6400000.45)
print(emp1.__salary)
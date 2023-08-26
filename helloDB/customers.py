class Customers():
    clients = []
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def infor_output(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Salary:', str(self.salary) + '$')
        
    def is_old_and_rich(self):
        if self.age >= 50 and self.salary > 1000000:
            return True
        else: 
            return False
    
    def __str__(self) -> str:
        return (self.name + '-' + str(self.age)+ '-' + str(self.salary))
    
    def __hash__(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return f"({self.name},{self.age},{self.salary})"
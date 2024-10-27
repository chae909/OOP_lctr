class Person:
    def __init__(self, name:str)->None:
        self.name = name

    def greet(self, msg:str)->None:
        print(msg)

class Employer(Person):
    def __init__(self, name:str, position:str)->None:
        super().__init__(name)
        self.position = position

    def direct(self, msg:str)->None:
        print(msg)

    def __str__(self)->str:
        return f'{self.name}, position: {self.position}'

class Employee(Person):
    def __init__(self, name:str, dept:str)->None:
        super().__init__(name)
        self.dept = dept

    def work(self):
        print(f"'{self.name}' is working at '{self.dept}'")

    def __str__(self)->str:
        return f'{self.name}, department: {self.dept}'

if __name__ == '__main__':
    emps = [Employer('Jonn', 'CEO'),
            Employer('Jane', 'CIO'),
            Employee('Smith', 'Development'),
            Employee('Robert', 'Sales')]

    for emp in emps:
        emp.greet("How are you doing?")
        if isinstance(emp, Employer):
            emp.direct("Finish the work by 6.")
        elif isinstance(emp, Employee):
            emp.work()
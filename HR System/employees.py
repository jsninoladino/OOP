# employees.py

# Parent class
class Employee:
    # Each employee will have an id and name has their instance attributes
    def __init__(self, 
                 id:int, 
                 name:str) -> None:
        self.id = id
        self.name = name

# Child class of Employee
class SalaryEmployee(Employee):
    def __init__(self, 
                 id:int, 
                 name:str, 
                 weekly_salary:int) -> None:
        # will have same instance attributes
        # avoids having to type
        # self.id = id
        # self.name = name
        super().__init__(id, 
                         name)
        # instance attribute unique to Salaried Employee
        self.weekly_salary = weekly_salary

    def calculate_payroll(self) -> int:
        return self.weekly_salary

# Child class of Employee
class HourlyEmployee(Employee):
    def __init__(self, 
                 id: int, 
                 name: str, 
                 hours_worked: float, 
                 hour_rate: float) -> None: 
        super().__init__(id, 
                         name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self) -> float:
        return self.hours_worked * self.hour_rate

# Child class of SalaryEmployee
class CommissionEmployee(SalaryEmployee):
    def __init__(self, 
                 id: int, 
                 name: str, 
                 weekly_salary: int, 
                 commission: int) -> None:
        super().__init__(id, 
                         name, 
                         weekly_salary)
        self.commission = commission

    def calculate_payroll(self) -> int:
        fixed = super().calculate_payroll()
        return fixed + self.commission

# Child class of SalaryEmployee
class Manager(SalaryEmployee):
    def work(self, 
             hours:int) -> None:
        print(f'{self.name} screams and yells for {hours} hours.')

# Child class of SalaryEmployee
class Secretary(SalaryEmployee):
    def work(self, 
             hours:int) -> None:
        print(f'{self.name} expends {hours} hours doing office paperwork.')

# Child class of CommissionEmployee
class SalesPerson(CommissionEmployee):
    def work(self, 
             hours:int) -> None:
        print(f'{self.name} expends {hours} hours on the phone.')

# Child class of HourlyEmployee
class FactoryWorker(HourlyEmployee):
    def work(self, 
             hours:int) -> None:
        print(f'{self.name} manufactures gadgets for {hours} hours.')

class TemporarySecretary(HourlyEmployee, Secretary):
    def __init__(self,
                 id:int,
                 name:str,
                 hours_worked:int,
                 hour_rate:float) -> None:
        super().__init__(id,
                         name,
                         hours_worked,
                         hour_rate)
# hr.py

class PayrollSystem:
    def calculate_payroll(self, employees:object):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')

# Parent class
class Employee:
    # Each employee will have an id and name has their instance attributes
    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name

# Child class of Employee
class SalaryEmployee(Employee):
    def __init__(self, id:int, name:str, weekly_salary:int) -> None:
        # will have same instance attributes
        # avoids having to type
        # self.id = id
        # self.name = name
        super().__init__(id, name)
        # instance attribute unique to Salaried Employee
        self.weekly_salary = weekly_salary

    def calculate_payroll(self) -> int:
        return self.weekly_salary

# Child class of Employee
class HourlyEmployee(Employee):
    def __init__(self, id: int, name: str, hours_worked: float, hour_rate: float) -> None: 
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

        def calculate_payroll(self) -> float:
            return self.hours_worked * self.hour_rate

# Child class of Salary Employee
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id: int, name: str, weekly_salary: int, commission: int) -> None:
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self) -> int:
        fixed = super().calculate_payroll(self)
        return fixed + self.commission
# hr.py

class PayrollSystem:
    def calculate_payroll(self, employees:object):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            if employee.address:
                print('-Sent to:')
                print(employee.address)
            print('')


# Child class of Employee
class SalaryPolicy:
    def __init__(self,
                 weekly_salary:int) -> None:
        # instance attribute unique to Salaried Policy
        self.weekly_salary = weekly_salary

    def calculate_payroll(self) -> int:
        return self.weekly_salary

# Child class of Employee
class HourlyPolicy:
    def __init__(self, 
                 hours_worked: float, 
                 hour_rate: float) -> None: 
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self) -> float:
        return self.hours_worked * self.hour_rate

# Child class of Salary Employee
class CommissionPolicy(SalaryPolicy):
    def __init__(self, 
                 weekly_salary: int, 
                 commission: int) -> None:
        # will have same instance attributes as SalaryPolicy instance attributes
        # avoids having to type
        # self.weekly_salary = weekly_salary
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self) -> int:
        fixed = super().calculate_payroll()
        return fixed + self.commission


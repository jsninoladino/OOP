# employees.py

import hr
import productivity

# Parent class
class Employee:
    # Each employee will have an id and name has their instance attributes
    def __init__(self, 
                 id: int, 
                 name: str) -> None:
        self.id = id
        self.name = name
        self.address = None

# Child class of SalaryEmployee
class Manager(Employee, 
              productivity.ManagerRole, 
              hr.SalaryPolicy):
    def __init__(self, 
                 id: int, 
                 name: str,
                 weekly_salary: int) -> None:
        # avoids having to write
        # self.weekly_salary = weekly_salary
        hr.SalaryPolicy.__init__(self,
                                 weekly_salary) 
        # avoids having to write
        # self.id = id
        # self.name = name
        super().__init__(id, 
                         name)

# Child class of SalaryEmployee
class Secretary(Employee, 
                productivity.SecretaryRole, 
                hr.SalaryPolicy):
    def __init__(self,
                 id: int,
                 name: str,
                 weekly_salary: int) -> None:
        hr.SalaryPolicy.__init__(self,
                                 weekly_salary)
        super().__init__(id, 
                         name)

# Child class of CommissionEmployee
class SalesPerson(Employee, 
                  productivity.SalesRole, 
                  hr.CommissionPolicy):
    def __init__(self, 
                 id: int, 
                 name: str,
                 weekly_salary: int,
                 commission: int) -> None:
        hr.CommissionPolicy.__init__(self,
                                     weekly_salary,
                                     commission)
        super().__init__(id, 
                         name)

# Child class of HourlyEmployee
class FactoryWorker(Employee, 
                    productivity.FactoryRole, 
                    hr.HourlyPolicy):
    def __init__(self, 
                 id: int, 
                 name: str,
                 hours_worked:int,
                 hour_rate:float) -> None:
        hr.HourlyPolicy.__init__(self,
                                 hours_worked,
                                 hour_rate)
        super().__init__(id, 
                         name)

class TemporarySecretary(Employee, 
                         productivity.FactoryRole, 
                         hr.HourlyPolicy):
    def __init__(self,
                 id:int,
                 name:str,
                 hours_worked:int,
                 hour_rate:float) -> None:

        hr.HourlyPolicy.__init__(self,
                                 hours_worked,
                                 hour_rate)
        super().__init__(id,
                         name)

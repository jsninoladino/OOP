# productivity.py

class ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }

    def get_role(self,
                 role_id:int):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type

    def track(self, 
              employees:list, 
              hours:int) -> None:
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}:{result}')
        print('')

class ManagerRole:
    def work(self,    
             hours:int) -> str:
        return f'screams and yells for {hours} hours.'

class SecretaryRole:
    def work(self,
             hours:int) -> str:
        return f'expends {hours} hours doing office paperwork.'

class SalesRole:
    def work(self,
             hours:int) -> str:
        return f'expends {hours} hours on the phone.'

class FactoryRole:
    def work(self,
             hours:int) -> str:
        return f'manufactures gadgets for {hours} hours.'
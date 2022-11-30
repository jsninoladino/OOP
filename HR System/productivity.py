# productivity.py

class ProductivitySystem:
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
             hours:int)""
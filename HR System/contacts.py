# contacts.py

class Address:
    def __init__(self,
                 street:str,
                 city:str,
                 state:str,
                 zipcode:str,
                 street2:str ='') -> None:
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self) -> str:
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)
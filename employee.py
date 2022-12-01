"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""




from abc import get_cache_token
from multiprocessing.spawn import get_command_line
from pkg_resources import working_set
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.commission_price = 0
        self.commission_amount = 1
        self.work_hour = 1

    def get_pay(self):
        return self.salary

    def get_commission(self):
        if self.commission_amount == 1:
            return self.commission_price
        else:
            return (self.commission_price * self.commission_amount)

    def __str__(self):
        return self.name


class MonthlyEmployee(Employee):
    def __init__(self, name, salary, commission_price=0, commission_amount=1):
        super().__init__(name, salary)
        self.commission_price = commission_price
        self.commission_amount = commission_amount

    def get_pay(self):
        total_salary = self.get_commission() + self.salary
        return total_salary

    def __str__(self):
        if self.commission_price == 0:
            return (f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}.")
        elif self.commission_price > 0 and self.commission_amount == 1:
            return (f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission_price}.  Their total pay is {self.get_pay()}.")
        elif self.commission_price > 0 and self.commission_amount > 0:
            return (f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.commission_amount} contract(s) at {self.commission_price}/contract.  Their total pay is {self.get_pay()}.")


class HourlyEmployee(Employee):
    def __init__(self, name, salary, work_hour, commission_price=0, commission_amount=1):
        super().__init__(name, salary)
        self.work_hour = work_hour
        self.commission_price = commission_price
        self.commission_amount = commission_amount

    def get_pay(self):
        total_salary = self.get_commission() + (self.work_hour * self.salary)
        return total_salary

    def __str__(self):
        if self.commission_price == 0:
            return (f"{self.name} works on a contract of {self.work_hour} hours at {self.salary}/hour.  Their total pay is {self.get_pay()}.")
        elif self.commission_price > 0 and self.commission_amount == 1:
            return (f"{self.name} works on a contract of {self.work_hour} hours at {self.salary}/hour and receives a bonus commission of {self.commission_price}.  Their total pay is {self.get_pay()}.")
        elif self.commission_price > 0 and self.commission_amount > 1:
            return (f"{self.name} works on a contract of {self.work_hour} hours at {self.salary}/hour and receives a commission for {self.commission_amount} contract(s) at {self.commission_price}/contract.  Their total pay is {self.get_pay()}.")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 30, 120, 600)

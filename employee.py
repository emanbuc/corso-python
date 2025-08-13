class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def calculate_paycheck(self):
        # Assuming a simple calculation where paycheck is salary divided by 12
        return self.salary / 52
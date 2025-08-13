from employee import Employee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise ValueError("Only Employee instances can be added")

    def display_employees(self):
        for emp in self.employees:
            print(f"Employee: {emp.fname} {emp.lname}, Salary: {emp.salary}, Paycheck: {emp.calculate_paycheck()}")

    def pay_employees(self):
        for emp in self.employees:
            paycheck = emp.calculate_paycheck()
            print(f"Paying {emp.fname} {emp.lname}: ${paycheck:.2f}")


def main():
    my_company = Company()
    emp1 = Employee("John", "Doe", 60000)
    my_company.add_employee(emp1)
    print(f"Added employee: {emp1.fname} {emp1.lname} with salary {emp1.salary}")

    emp2 = Employee("Jane", "Smith", 75000)
    my_company.add_employee(emp2)
    print(f"Added employee: {emp2.fname} {emp2.lname} with salary {emp2.salary}")

    my_company.display_employees()
    my_company.pay_employees()


if __name__ == "__main__":
    main()

        


import datetime


class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date


class Company:
    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        print(f"\n{self.name} employees:")
        if self.employees:
            print("* " + "\n* ".join(employee.name for employee in self.employees))
        else:
            print("There are no employees.")


umbrella_co = Company("Umbrella", "123 Zombie Way", "Pharmaceuticals")
slacker_co = Company("Slacker, Inc.", "987 Meh Street", "Procrastination")

rey = Employee("Rey", "Jedi", datetime.datetime.now().date())
antman = Employee("Scott Lang", "Electric Engineer", datetime.datetime.now().date())
glokta = Employee("Savine dan Glokta", "Entrepreneur", datetime.datetime.now().date())
rogers = Employee("Steve Rogers", "Captain", datetime.datetime.now().date())
katarn = Employee("Kyle Katarn", "Jedi", datetime.datetime.now().date())

slacker_co.add_employee(antman)
slacker_co.add_employee(glokta)
umbrella_co.add_employee(rogers)
umbrella_co.add_employee(rey)
umbrella_co.add_employee(katarn)


slacker_co.print_employees()
umbrella_co.print_employees()

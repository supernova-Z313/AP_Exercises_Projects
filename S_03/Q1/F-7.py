# Q7: Employee Parsing
# https://edabit.com/challenge/j2HauiSdDadkjxjsQ
# notes in question
class Employee:
    def __init__(self, fi, la, mo):
        self.firstname = fi
        self.lastname = la
        self.salary = mo

    def from_string(arg: str):
        e1, e2, e3 = arg.split("-")
        e3 = int(e3)
        return Employee(e1, e2, e3)


if __name__ == "__main__":
    emp1 = Employee("Mary", "Sue", 60000)
    emp2 = Employee.from_string("John-Smith-55000")

    print(emp2.firstname)
    print(emp2.lastname)
    print(emp2.salary)

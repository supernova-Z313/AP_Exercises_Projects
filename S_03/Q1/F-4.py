# Q4: FullName and Email
# https://edabit.com/challenge/gB7nt6WzZy8TymCah
# notes in question
class Employee:
    def __init__(self, f: str, las: str):
        self.firstname = f
        self.lastname = las
        self.fullname = "{} {}".format(self.firstname, self.lastname)
        self.email = "{}.{}@company.com".format(self.firstname.lower(), self.lastname.lower())


if __name__ == "__main__":
    emp_2 = Employee("Mary",  "Sue")
    print(emp_2.email)

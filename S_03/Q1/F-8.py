# Q8:Employee Class with Keywords
# https://edabit.com/challenge/S7rdJsn6vkfC9BzcR
# notes in question
class Employee:
    def __init__(self, args, **kwargs):
        args = args.split(" ")
        if len(args) == 2:
            self.name = args[0]
            self.lastname = args[1]
        else:
            self.name = args[0]

        for i in kwargs:
            setattr(self, i, kwargs[i])


if __name__ == "__main__":
    john = Employee("John Doe")
    mary = Employee("Mary Major", salary=120000)
    richard = Employee("Richard Roe", salary=110000, height=178)

    print(john.name)
    print(mary.lastname)

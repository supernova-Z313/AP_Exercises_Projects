# Q1: Older than me
# https://edabit.com/challenge/JFLADuABfkeoz8mqN
# notes in question
class Person:
    def __init__(self, n: str, a: int):
        self.name = n
        self.age = a

    def compare_age(self, person2):
        if self.age > person2.age:
            return "{} is younger than me.".format(person2.name)

        elif self.age < person2.age:
            return "{} is older than me.".format(person2.name)

        else:
            return "{} is the same age as me.".format(person2.name)


if __name__ == "__main__":
    p1 = Person("Samuel", 24)
    p2 = Person("Joel", 36)
    p3 = Person("Lily", 24)

    print(p1.compare_age(p2))

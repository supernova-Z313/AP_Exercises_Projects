# Q5: Count Number of Instances
# https://edabit.com/challenge/rprukfcGWqnvKZR9g
# notes in question
class User:
    user_count = 0

    def __init__(self, name):
        User.user_count += 1
        self.username = name


if __name__ == "__main__":
    u1 = User("john smith 10")
    print(User.user_count)


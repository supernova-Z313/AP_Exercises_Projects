# Q6: BookShelf
# https://edabit.com/challenge/uK4Dw7Pise5uCfKqo
# notes in question
class Book:
    def __init__(self, t: str, o: str):
        self.title = t
        self.author = o

    def get_title(self):
        return "Title: {}".format(self.title)

    def get_author(self):
        return "Author: {}".format(self.author)


if __name__ == "__main__":
    PP = Book("Pride and Prejudice", "Jane Austen")
    H = Book("Hamlet", "William Shakespeare")
    WP = Book("War and Peace", "Leo Tolstoy")

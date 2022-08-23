class Book:
    def __init__(self, idb, name, cou):
        # set the first information
        self.name_b = name
        self.ID_book = idb
        self.counter = int(cou)

    def book_number(self, con, das=True):
        """change number of book"""
        if das:
            self.counter += con
        else:
            self.counter -= con


class LibraryMember:
    def __init__(self, idm, name):
        # set the first information
        self.ID_P = idm
        self.name_P = name
        self.save_book = []

    def list_book(self, b_id, das=True):
        """update list of borrowed books"""
        if das:
            self.save_book.append(b_id)
        else:
            self.save_book.remove(b_id)


class Library:
    def __init__(self):
        # Create a library with empty book lists and members
        self.members = {}
        self.Books = {}

    def add_book(self, id_b, name, count):
        # add book to list of book
        self.Books[id_b] = Book(id_b, name, count)

    def add_member(self, id_m, name):
        # add member
        self.members[id_m] = LibraryMember(id_m, name)

    def get(self, member_id, book_id):
        """check the rule and if there is no problem
        add book to list of borrow books of that member"""
        if len(self.members[member_id].save_book) == 5:
            print("MaxReached : {} {}".format(self.members[member_id].name_P, member_id))
        elif self.Books[book_id].counter < 1:
            print("NotAvailable : {} {}".format(self.Books[book_id].name_b, book_id))
        else:
            self.Books[book_id].book_number(1, das=False)
            self.members[member_id].list_book(book_id, das=True)

    def returned(self, member_id, book_id):
        """Update the list of borrowed books and
        add the existing book in the relevant list"""
        self.members[member_id].list_book(book_id, das=False)
        self.Books[book_id].book_number(1, das=True)

    def member_stat(self):
        # show the state of member on form
        print("----------------------------------------------------------")

        for i in self.members:
            print(self.members[i].name_P, i)
            for j in self.members[i].save_book:
                print("    - {} {}".format(self.Books[j].name_b, j))
            print()

        print("----------------------------------------------------------")

    def command(self, entry: str):
        """get commands from input and Process them and
         send them to the relevant command"""
        inp: list = entry.split("(")
        inp[1] = inp[1][0:-1]
        inp[1] = inp[1].split(",")
        inp[1].remove("self")
        for ind, i in enumerate(inp[1]):
            inp[1][ind] = inp[1][ind].strip()

        if inp[0] == "addBook":
            self.add_book(*inp[1])

        elif inp[0] == "addMember":
            self.add_member(*inp[1])

        elif inp[0] == "get":
            self.get(*inp[1])

        elif inp[0] == "return":
            self.returned(*inp[1])

        else:
            self.member_stat()


if __name__ == "__main__":
    # get the name of library
    lib_name = input("enter the library name: ")
    # set the library name and start the commands
    globals()[lib_name] = Library()
    com = input()
    while com != "END":
        globals()[lib_name].command(com)
        com = input()

# test case:
"""
my_lib
addBook(self, a1, name, 5)
addBook(self, 2b, phis, 2)
addBook(self, 3b, math, 1)
addBook(self, a2, ap, 10)
addMember(self, 100, ahmad)
addMember(self, 101, ali)
addMember(self, 102, aye)
get(self, 101, 2b)
get(self, 101, a1)
get(self, 101, a2)
get(self, 101, 2b)
get(self, 101, a2)
get(self, 100, 3b)
get(self, 100, 2b)
get(self, 101, a1)
get(self, 102, 3b)
get(self, 102, 2b)
get(self, 102, a2)
return(self, 101, 2b)
return(self, 100, 3b)
get(self, 102, 2b)
memberStat(self)
END
"""
# OUTPUT test case:
"""
NotAvailable : phis 2b
MaxReached : ali 101
NotAvailable : math 3b
NotAvailable : phis 2b
----------------------------------------------------------
ahmad 100

ali 101
    - name a1
    - ap a2
    - phis 2b
    - ap a2

aye 102
    - ap a2
    - phis 2b

----------------------------------------------------------
"""

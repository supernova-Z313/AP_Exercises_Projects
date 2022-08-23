
class MedadRangi:
    locations = (35.74317403843504, 51.50185488303431)
    __discount_rate = 10
    __Items = {}

    def __init__(self, name: str = "None", price: float = 0.0, number: int = 1, made_in: str = "Iran",
                 company: str = "None"):
        self.name = name
        self.price = price
        self.number = number
        self.made_in = made_in
        self.company = company
        self.f_price = 0
        MedadRangi.__Items[self.name] = self

    @staticmethod
    def final_price():
        all_item = {}
        for i in MedadRangi.__Items:
            MedadRangi.__Items[i].f_price = MedadRangi.__Items[i].price * (100-MedadRangi.__discount_rate) / 100
            all_item[MedadRangi.__Items[i].name] = MedadRangi.__Items[i].f_price
        return all_item

    @staticmethod
    def welcome():
        import datetime
        d = str(datetime.datetime.now())
        if 6 <= int(d[11:13]) < 12:
            print("Good Morning")
        elif 12 <= int(d[11:13]) < 18:
            print("Good Afternoon")

    @staticmethod
    def calculate_distance(x: float, y: float):
        from math import sqrt
        dis = sqrt((x - MedadRangi.locations[0])**2 + (y - MedadRangi.locations[1])**2)
        return dis

    @staticmethod
    def load_csv(name_of_file: str = "items"):
        import csv
        with open(f'{name_of_file}.csv') as file:
            full_list = csv.reader(file)
            for ind, i in enumerate(full_list):
                if ind == 0:
                    pass
                else:
                    obj = i[0].split("\t")
                    MedadRangi(obj[0], float(obj[1]), int(obj[2]), obj[3], obj[4])
            print(f"{ind} items successfully added")

    @staticmethod
    def see_all():
        print("| Row | {:^20} | {:^10} | {:^20} |".format("Name", "Numbers", "First Price"))
        print("==================================================================")
        for ind, i in enumerate(MedadRangi.__Items, start=1):
            print("|{:^5}|{:^22}|{:^12}|{:^22}|".format(ind, i, MedadRangi.__Items[i].number
                                                        , MedadRangi.__Items[i].price))
            print("------------------------------------------------------------------")


if __name__ == "__main__":
    MedadRangi.load_csv("items")
    MedadRangi.see_all()

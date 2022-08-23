import requests
import re
import csv
import threading
# دریافت تعداد سوالات در کوعرا با رجکس
class quera:
    def __init__(self, name, passw):
        self._name = name
        self._passw = passw

    def get_account_info(self, u_name):
        res = requests.get(f"https://quera.org/profile/{u_name}/activity")
        print(res)
        if res.status_code == 200:
            n = re.findall('font-variant-numeric:proportional-nums;}</style><dd class="chakra-stat__number css-1axeus7">(.*)<!-- --> ....<!', res.text)[0][-1]
        return n

    def get_accounts_info(self, name):
        with open(f"{name}.csv", "a") as csv_file:
            csv_r = csv.reader(csv_file, delimiter=',')
            def ne(x):
                requests.get(f"https://quera.org/profile/{x}/activity")
            for i in csv_r:

                d = threading.Thread()


if __name__ == "__main__":
    a = quera("aaa", "bbb")
    a.get_account_info("supernova313")

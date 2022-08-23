class Bank:
    # set some privet variable of class
    __transaction_counter = 99
    __interest_rate = 5
    __members = []
    __ids = []

    @staticmethod
    def __utc_time():
        """use a privet static method to get the utc time"""
        import datetime
        time_n = ((str(datetime.datetime.utcnow())[:19].replace("-", "")).replace(":", "")).replace(" ", "")
        return time_n

    @staticmethod
    def _interest_rate_set(value: int):
        """change the interest whit a protected static method"""
        setattr(Bank, "_Bank__interest_rate", value)

    @staticmethod
    def _transaction_counter_set(value: int):
        """change the transaction counter whit a protected method"""
        setattr(Bank, "_Bank__transaction_counter", value)

    @staticmethod
    def _pay_all_interest():
        """pay the interest of all member in one command and get
        all confirmation code in a dict"""
        all_fish = {}
        for i in Bank.__members:
            res = i.pay_interest()
            all_fish[i] = res
        return all_fish

    @staticmethod
    def confirmation_number(transaction_type, account_num, utc_time, transaction_id):
        """create confirmation code"""
        return "-".join([transaction_type, str(account_num), str(utc_time), str(transaction_id)])

    def __init__(self, account_number: int, first_name: str, last_name: str, timezone: int = +0, balance=0):
        # set first information
        if account_number in Bank.__ids:
            raise "There must be a unique account number"
        else:
            from decimal import getcontext, Decimal
            # set number of digit after .
            getcontext().prec = 7
            self.first_name = first_name
            self.last_name = last_name
            self.__full_name = self.first_name + self.last_name
            self._timezone = timezone
            self.__balance = Decimal(balance)
            self.__account_number = account_number
            # add member to list of bank member
            Bank.__members.append(self)

    @property
    def _full_name(self):
        """make a only read var"""
        self.__full_name = self.first_name + self.last_name
        return self.__full_name

    @property
    def _balance(self):
        """make a only read var"""
        return self.__balance

    @property
    def _account_number(self):
        """make a only read var"""
        return self.__account_number

    def deposit(self, amount: int):
        """deposit to account balance"""
        from decimal import getcontext, Decimal
        getcontext().prec = 7
        self.__balance += Decimal(amount)
        Bank.__transaction_counter += 1
        return Bank.confirmation_number("D", self.__account_number, Bank.__utc_time(), Bank.__transaction_counter)

    def withdrawal(self, amount: int):
        """withdrawal to account balance"""
        from decimal import getcontext, Decimal
        getcontext().prec = 7
        if amount > self.__balance:
            Bank.__transaction_counter += 1
            return Bank.confirmation_number("X", self.__account_number, Bank.__utc_time(), Bank.__transaction_counter)
        else:
            Bank.__transaction_counter += 1
            self.__balance -= Decimal(amount)
            return Bank.confirmation_number("W", self.__account_number, Bank.__utc_time(), Bank.__transaction_counter)

    def pay_interest(self):
        """pay interest to just this account"""
        from decimal import getcontext, Decimal
        getcontext().prec = 7
        self.__balance += Decimal((self.__balance*Bank.__interest_rate)/100)
        Bank.__transaction_counter += 1
        return Bank.confirmation_number("I", self.__account_number, Bank.__utc_time(), Bank.__transaction_counter)

    def confirmation_code_parser(self, text: str):
        """confirmation code parser"""
        # this is not a static method because for parser the time of transaction
        # we need the the time of person
        from collections import namedtuple
        sep = text.split("-")
        time_changer = sep[-2][8:]
        date_changer = int(sep[-2][:8])

        # if time more than 24 or less than 0 should do Related work
        if abs(self._timezone * 10000) >= int(time_changer):
            dispute = abs(self._timezone * 10000) - int(time_changer)
            time_changer = 240000 - dispute
            date_changer -= 1

        else:
            time_changer = int(time_changer) + (self._timezone * 10000)
            if time_changer > 240000:
                new_day = str(time_changer - 240000)
                new_day = "0"*(6-len(new_day)) + new_day
                time_changer = new_day
                date_changer += 1

        time_changer = str(time_changer)
        time_changer = time_changer[0:2] + ":" + time_changer[2:4] + ":" + time_changer[4:]
        date_changer = str(date_changer)
        date_changer = date_changer[0:4] + "-" + date_changer[4:6] + "-" + date_changer[6:]
        final_changer = date_changer + " " + time_changer
        utc_time = sep[2]
        utc_time = "{0}-{1}-{2} {3}:{4}:{5}".format(utc_time[0:4], utc_time[4:6], utc_time[6:8], utc_time[8:10],
                                                    utc_time[10:12], utc_time[12:])
        Result = namedtuple("Result", "transaction_code account_number time_utc transaction_id time")
        result = Result(sep[0], sep[1], utc_time, sep[3], final_changer)
        return result


if __name__ == "__main__":
    from unittest import TestCase, main
    # comment and docstring in github version

    P1 = Bank(1, "ahmad", "good", +5, 0)
    P2 = Bank(2, "ali", "nice", -6, 10)

    Bank._interest_rate_set(10)

    print(P1.deposit(10.12131851))
    # TestCase.assertEqual(P1.deposit(10.12131851), "D-2-20220329060000-102", "fk")
    # AttributeError: 'str' object has no attribute '_getAssertEqualityFunc'
    print(P2.pay_interest())
    print(P2.withdrawal(10))
    print(P2.withdrawal(10))
    # assert P1._balance == 10.1213, "Should be 10.1213"
    print(P1._balance)
    print(P2.confirmation_code_parser(P2.deposit(5)))
    # TestCase.assertTrue(TestCase, P2.confirmation_code_parser(P2.deposit(5)).account_number == "2")

    all_transaction = Bank._pay_all_interest()
    print(all_transaction)
    print(all_transaction[P1])
    # unittest.main()
    # AttributeError: 'str' object has no attribute '_getAssertEqualityFunc'

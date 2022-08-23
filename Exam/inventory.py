class Resource:
    def __init__(self, name: str = "i5", manufacturer: str = "intel", total: int = 1, allocated: int = 0):
        self._name = name
        self._manufacturer = manufacturer
        if not type(total)==type(allocated)==int:
            raise TypeError('total and allocated must be integers')
        self.__total = total
        self.__allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self.__total

    @property
    def allocated(self):
        return self.__allocated

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"name: {self._name}, manufacturer: {self._manufacturer}, total : {self.__total}"

    def claim(self, n: int = 1):
        if (n >= 0) and (str(type(n)) == "<class 'int'>") and (n <= self.__total):
            self.__allocated += n

    def freeup(self, n: int = 1):
        if (n >= 0) and (str(type(n)) == "<class 'int'>") and (n <= self.__allocated):
            self.__allocated -= n

    def died(self, n :int = 1):
        if (n >= 0) and (str(type(n)) == "<class 'int'>") and (n <= self.__total):
            self.__total -= n

    def purchased(self, n :int = 1):
        if (n >= 0) and (str(type(n)) == "<class 'int'>"):
            self.__total += n

    def c_name(self):
        return (type(self).__name__).lower()

    category = property(c_name)


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated , cores: int = 4, socket: str = "amd64", power_watts: int = 94):
        self.cores = cores
        self.socket = socket
        self.power_watts = power_watts
        super(CPU, self).__init__(name, manufacturer, total, allocated)


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        if type(capacity_GB) != int:
            raise TypeError('capacity_GB is nt integer')

        self._capacity_GB = capacity_GB

    @property
    def capacity_GB(self):
        return self._capacity_GB


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, size: float, rpm: int):
        self._size = size
        self._rpm = rpm
        super(HDD, self).__init__(name, manufacturer, total, allocated)

    @property
    def size(self):
        return self.size

    @property
    def rpm(self):
        return self.rpm

    def __repr__(self):
        return f"size: {self.size}"


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, interface: str, *args):
        self._interface = interface
        super(SSD, self).__init__(name, manufacturer, total, allocated)

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return f"interface: {self._interface}"


if __name__ == "__main__":
    pass

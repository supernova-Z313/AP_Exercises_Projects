import math

def Arcsinus(a):
        global taf, st, en, vas, sin_m
        st = math.pi/2
        en = (-1*(math.pi))/2
        vas = 0.0
        sin_m = math.sin(0)
        taf = abs(st - en)
        def inner(b):
            global taf, st, en, vas, sin_m
            while taf/2 > a:
                if sin_m > b:
                    st = vas
                    vas = (st+en)/2
                    sin_m = math.sin(vas)
                    taf = abs(st - en)
                else:
                    en = vas
                    vas = (st+en)/2
                    sin_m = math.sin(vas)
                    taf = abs(st - en)
            return vas
        return inner

degat, number = input().split(" ")
degat, number = float(degat), float(number)

Arcsin_a = Arcsinus(degat)
print(round(Arcsin_a(number), 4))

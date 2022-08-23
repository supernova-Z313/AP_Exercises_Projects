def factorial(n):
    x = 1
    c = (2*n + 1)+1
    for i in range(1, c):
        x *= i
    return x

# ======================================================================
def sinus(a, b):
    b = (b * 3.14) / 180
    def inner():
        finallnum = 0
        for i in range(a):
            z = factorial(i)
            finallnum += (((-1)**i)*(b**(2*i+1)))/z
        return finallnum
    return inner()

bast, zavie = input().split(" ")
bast, zavie = int(bast), float(zavie)
anw = sinus(bast, zavie)
print(round(anw,6))
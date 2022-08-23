import re
numbers = ["0","1","2","3","4","5","6","7","8","9"]

def fesh(a):
    st = ""
    f = a[0]
    con = 0
    s = 1
    a += "1"
    for i in a:
        if i == 1:
            if con == 0:
                st += f
                f = i
            else:
                st = st + f+ str(con+1)
        if s == 1:
            s +=1
        else:
            if i == f:
                con += 1
            else:
                if con == 0:
                    st += f
                    f = i
                else:
                    st = st + f+ str(con+1)
                    f = i
                    con = 0
    return st


def gost(a):
    global numbers
    st = ""
    n = a[0]
    k = re.findall('[0-9]+',a)
    co = 0
    for i in a:
        if i in numbers:
            if not(n == ""):
                # print(k[co])
                # print(type(k[co]))
                st = st + (n*(int(k[co])-1))
                co += 1
                n = ""
        else:
            st += i
            n = i
    return st


t = int(input())
all =  []
for i in range(t):
    h = int(input())
    word = input()
    if h == 1:
        all.append(fesh(word))
    else:
        all.append(gost(word))

for i in all:
    print(i)

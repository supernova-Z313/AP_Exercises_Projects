# fuck this life

earth = {}
for i in range(1, 7):
    for j in range(1, 8):
        earth[(i,j)] = 0


#=====================================================================
def tagirat(a, b):
    global earth
    j = 1
    while not(earth[(j, a)] == 0):
        j += 1
    
    earth[(j, a)] = b

#=====================================================================
def shape(a):
    all = []
    yed = []
    for i in a:
        yed.append(a[i])
        if len(yed) == 7:
            all.append(yed)
            yed = []
    all.reverse()
    for i in all:
        for index,j in enumerate(i):
            if index == 0:
                print(j,end="")
            elif index == 6:
                print(" ", j)
            else:
                print(" ", j,end="")

#=====================================================================
def natige(a):
    for i in a:
        team = a[i]
        if team != 0:
            
            s, e = i
            cou = 0
            for j in range(4):
                if (s, e+j) in a:
                    if team == a[(s, e+j)]:
                        cou += 1
            # print(cou)
            if cou == 4:
                return team
            

            s, e = i
            cou = 0
            for j in range(4):
                if (s+j, e) in a:
                    if team == a[(s+j, e)]:
                        cou += 1
            # print(cou)
            if cou == 4:
                return team
            
            
            s, e = i
            cou = 0
            for j in range(4):
                if (s+j, e+j) in a:
                    if team == a[(s+j, e+j)]:
                        cou += 1
            # print(cou)
            if cou == 4:
                return team

            
            s, e = i
            cou = 0
            for j in range(4):
                if (s-j, e+j) in a:
                    if team == a[(s-j, e+j)]:
                        cou += 1
            # print(cou)
            if cou == 4:
                return team

#=====================================================================
t = int(input())
h = input().split(" ")
h1 = []
for i in h:
    h1.append(int(i))


for index,i in enumerate(h1):
    if index%2 == 0:
        tagirat(i, "r")
    else:
        tagirat(i, "y")

win = natige(earth)


print("Winner = ", win)
shape(earth)





a, b, c = input().split(" ")

loc = {}
color = 1

for i in range(1,int(a)+1):
    for j in range(1,int(b)+1):
        loc[(i, j)] = []

for i in range(int(c)):
    s,e,z = input().split(" ")
    s,e,z = int(s),int(e),int(z)
    # loc[(s,e)] += [color]
    for j in range(z):
        for h in range(z):
            loc[(s+j, e+h)] += [color]
    color += 1


finall = []

for i in loc.values():
  if not(i in finall):
      finall.append(i)

if [] in finall:
    print(len(finall)-1)
else:
    print(len(finall))

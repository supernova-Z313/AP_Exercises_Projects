
t , p ,q = input().split(" ")
p = int(p)
q = int(q)
names = {}
for i in range(int(t)):
    v = input()
    v_f = v[0:p]
    v_e = v[len(v)-q:]
    if v_f in names:
        if not(v_e == names[v_f]):
            names[v_f] = v_e
    else:
        names[v_f] = v_e

print(len(names))

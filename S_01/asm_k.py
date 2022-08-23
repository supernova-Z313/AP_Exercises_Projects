
a, b, c = input().split(" ")
a, b, c = int(a),int(b),int(c)
all_w = []

for i in range(b):
    w = input().split()
    all_w.append(w)

all_num = {}
for i in range(a):
    all_num[i] = 0

all_w_e = []
for i in range(b):
    all_w_e.append([])


for k in range(c):
    all_kal = {}
    
    all_w_e = []
    for i in range(b):
        all_w_e.append([])


    h = input()
    for i in range(a):
        nf = input().split(" ")
        all_kal[i] = nf
        for j in range(b):
            if (nf[j] in all_w[j]) and (nf[j][0] == h):
                all_w_e[j].append(nf[j])
    
    
    for i in all_kal:
        cou = 0
        for j in all_kal[i]:
            # print(j)
            # print(all_w_e[cou])
            em = all_w_e[cou].count(j)
            cou += 1
            # print(em)
            if em == 1:
                all_num[i] += 10
            if em >= 2:
                all_num[i] += 5
            
            # print(all_num,end="\n\n\n")

    # print(all_w_e,end="\n\n\n")
    # print(all_kal,end="\n\n\n")
    # print(all_num,end="\n\n\n")
    # print(all_w,end="\n\n\n")

fin = []
for i in all_num:
    fin.append(str(all_num[i]))

# print(fin)
s = " ".join(fin)

print(s)



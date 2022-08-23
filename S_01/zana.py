

t = int(input())
names_m = {}
tatib = []
for i in range(t):
    n = input()
    tatib.append(n)
    names_m[n] = 0

sec_money = names_m.copy()
names_f = {}

for i in range(t):
    na = input()
    money, f = input().split(" ")
    names_m[na] = int(money) 
    fri_list = []
    fri_list.append(int(f))
    for j in range(int(f)):
        fri = input()
        fri_list.append(fri)
    names_f[na] = fri_list


# print(names_m,end="\n\n\n\n")

for i in names_m:
    if names_f[i][0] == 0:
        gift = 0
        bagi = names_m[i]
    else:
        gift = names_m[i]//names_f[i][0]
        bagi = names_m[i]%names_f[i][0]
    # print(i, "  ",bagi)
    sec_money[i] += bagi
    for j in names_f[i][1:]:
        sec_money[j] += gift
    # print(sec_money,end="\n\n\n\n")

# print(sec_money,end="\n\n\n\n\n")
# print(names_m,end="\n\n\n\n\n")
# print(names_f,end="\n\n\n\n\n")


for name in tatib:
    print(name ," ", (sec_money[name]-names_m[name]))


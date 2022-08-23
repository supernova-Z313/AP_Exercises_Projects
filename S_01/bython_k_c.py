import re

all_com = []
all_inp = {}
all_inp_t = []
v_cou = 0
one_l = ""
while one_l != "-----":
    one_l = input()
    if one_l == "-----":
        pass
    else:
        all_com.append(one_l)


for i in all_com:
    
    x = re.findall('agar (.+) == (.+) : (.+)', i)
    if x != []:
        x = list(x[0])
        if x[0] in all_inp:
            if x[1] in all_inp:
                if all_inp[x[0]] == all_inp[x[1]]:

                    xx = re.findall('(.+) = voroodi\(\)',i)
                    if xx != []:
                        on1 = int(input())
                        all_inp[xx[0]] = on1
                        continue

                    x1 = re.findall('(.+) = ([0-9]+|.+) (.) ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f)
                        v_cou += 1
                        if gos[2] == "+":
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] + all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] + all_inp[gos[3]]
                                    continue
                        else:
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] - all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] - all_inp[gos[3]]
                                    continue


                    

                        
                    x1 = re.findall('(.+) = ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f)                
                        try:
                            all_inp[gos[0]] = int(gos[1])
                            continue
                        except:
                            all_inp[gos[0]] = all_inp[gos[1]]
                            continue
                else:
                    continue
        
            else:
                if all_inp[x[0]] == int(x[1]):

                    xx = re.findall('(.+) = voroodi\(\)',i)
                    if xx != []:
                        on1 = int(input())
                        all_inp[xx[0]] = on1
                        continue

                    x1 = re.findall('(.+) = ([0-9]+|.+) (.) ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f)
                        v_cou += 1
                        if gos[2] == "+":
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] + all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] + all_inp[gos[3]]
                                    continue
                        else:
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] - all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] - all_inp[gos[3]]
                                    continue
                    

                    

                        
                    x1 = re.findall('(.+) = ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f)                
                        try:
                            all_inp[gos[0]] = int(gos[1])
                            continue
                        except:
                            all_inp[gos[0]] = all_inp[gos[1]]
                            continue
                else:
                    continue
        
        else:
            if x[1] in all_inp:
                if int(x[0]) == all_inp[x[1]]:
                    xx = re.findall('(.+) = voroodi\(\)',i)
                    if xx != []:
                        on1 = int(input())
                        all_inp[xx[0]] = on1
                        continue

                    x1 = re.findall('(.+) = ([0-9]+|.+) (.) ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f)
                        v_cou += 1
                        if gos[2] == "+":
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] + all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] + all_inp[gos[3]]
                                    continue
                        else:
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] - all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] - all_inp[gos[3]]
                                    continue


                    


                    x1 = re.findall('(.+) = ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f)                
                        try:
                            all_inp[gos[0]] = int(gos[1])
                            continue
                        except:
                            all_inp[gos[0]] = all_inp[gos[1]]
                            continue
                else:
                    continue
            else:
                if int(x[0]) == int(x[1]):
                    xx = re.findall('(.+) = voroodi\(\)',i)
                    if xx != []:
                        on1 = int(input())
                        all_inp[xx[0]] = on1
                        continue

                    x1 = re.findall('(.+) = ([0-9]+|.+) (.) ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f)
                        v_cou += 1
                        if gos[2] == "+":
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] + all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] + gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] + all_inp[gos[3]]
                                    continue
                        else:
                            try:
                                gos[1] = int(gos[1])
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = gos[1] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = gos[1] - all_inp[gos[3]]
                                    continue
                            except:
                                try:
                                    gos[3] = int(gos[3])
                                    all_inp[gos[0]] = all_inp[gos[1]] - gos[3]
                                    continue
                                except:
                                    all_inp[gos[0]] = all_inp[gos[1]] - all_inp[gos[3]]
                                    continue
                    


            



                    x1 = re.findall('(.+) = ([0-9]+|.+)', x[2])
                    if x1 != []:
                        gos = []
                        for j in x1:
                            for f in j:
                                if f != '':
                                    gos.append(f) 
                                       
                        try:
                            all_inp[gos[0]] = int(gos[1])
                            continue
                        except:
                            all_inp[gos[0]] = all_inp[gos[1]]
                            continue
                else:
                    continue
    
    
    x = re.findall('(.+) = voroodi\(\)',i)
    if x != []:
        on1 = int(input())
        all_inp[x[0]] = on1
        continue

    x = re.findall('(.+) = ([0-9]+|.+) (.) ([0-9]+|.+)', i)
    # print(x)
    if x != []:
        gos = []
        for j in x:
            for f in j:
                if f != '':
                    gos.append(f)
        v_cou += 1
        if gos[2] == "+":
            try:
                gos[1] = int(gos[1])
                try:
                    gos[3] = int(gos[3])
                    all_inp[gos[0]] = gos[1] + gos[3]
                    continue
                except:
                    all_inp[gos[0]] = gos[1] + all_inp[gos[3]]
                    continue
            except:
                try:
                    gos[3] = int(gos[3])
                    all_inp[gos[0]] = all_inp[gos[1]] + gos[3]
                    continue
                except:
                    all_inp[gos[0]] = all_inp[gos[1]] + all_inp[gos[3]]
                    continue
        else:
            try:
                gos[1] = int(gos[1])
                try:
                    gos[3] = int(gos[3])
                    all_inp[gos[0]] = gos[1] - gos[3]
                    continue
                except:
                    all_inp[gos[0]] = gos[1] - all_inp[gos[3]]
                    continue
            except:
                try:
                    gos[3] = int(gos[3])
                    all_inp[gos[0]] = all_inp[gos[1]] - gos[3]
                    continue
                except:
                    all_inp[gos[0]] = all_inp[gos[1]] - all_inp[gos[3]]
                    continue
    
    x = re.findall('(.+) = ([0-9]+|.+)', i)
    if x != []:
        gos = []
        for j in x:
            for f in j:
                if f != '':
                    gos.append(f)
        # v_cou += 1
        try:
            all_inp[gos[0]] = int(gos[1])
            continue
        except:
            all_inp[gos[0]] = all_inp[gos[1]]
            continue
    

    x = re.findall('khoorooji\((.+)\)', i)
    if x != []:
        x1 = "".join(x)
        x1 = x1.split(", ")
        b = 0
        for j in x1:
            if b == 0:
                b += 1
            else:
                print(" ",end="")
            if j in all_inp:
                print(all_inp[j], end="")
            else:
                print(int(j), end="")
        print("")


print(len(all_inp))

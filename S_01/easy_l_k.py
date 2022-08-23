import re

players = {}
player_co = 1

teams = {}
team_co = 1
teams_e = {}

team_p ={}
buy_c = []

while True:
    com = input()
    if com == "":
        pass
    elif com == "end":
        break
    else:

        x = re.findall('new player (.+) ([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)', com)
        if x != []:
            x = list(x[0])
            for index, i in enumerate(x):
                if index > 0:
                    x[index] = int(i)
            players[player_co] = x
            buy_c.append(player_co)
            player_co += 1
            continue

        
        x = re.findall('new team (.+) ([0-9]+)', com)
        if x != []:
            x = list(x[0])
            for index, i in enumerate(x):
                if index > 0:
                    x[index] = int(i)
            teams[team_co] = x
            team_p[team_co] = []
            teams_e[team_co] = [0, 0, -(team_co)]
            team_co += 1
            continue
            

        x = re.findall('buy ([0-9]+) ([0-9]+)', com)
        if x != []:
            x = list(x[0])
            for index, i in enumerate(x):
                x[index] = int(i)
            if not(x[0] in players):
                print("player with the id playerID doesnt exist")
                continue
            elif not(x[1] in teams):
                print("team with the id teamID doesnt exist")
                continue
            elif not(teams[x[1]][1] >= players[x[0]][1]):
                print("the team cant afford to buy this player")
                continue
            elif not(x[0] in buy_c):
                print("player already has a team")
                continue
            else:
                print("player added to the team succesfully")
                buy_c.remove(x[0])
                team_p[x[1]].append(x[0])
                teams[x[1]][1] = teams[x[1]][1] - players[x[0]][1]
                continue

        
        x = re.findall('sell ([0-9]+) ([0-9]+)', com)
        if x != []:
            x = list(x[0])
            for index, i in enumerate(x):
                x[index] = int(i)
            if not(x[1] in teams):
                print("team doesnt exist")
                continue
            elif not(x[0] in team_p[x[1]]):
                print("team doesnt have this player")
                continue
            else:
                print("player sold succesfully")
                buy_c.append(x[0])
                team_p[x[1]].remove(x[0])
                teams[x[1]][1] = teams[x[1]][1] + players[x[0]][1]
                continue
        

        x = re.findall('match ([0-9]+) ([0-9]+)', com)
        if x != []:
            x = list(x[0])
            for index, i in enumerate(x):
                x[index] = int(i)
            if (x[0] not in teams) or (x[1] not in teams):
                print("team doesnt exist")
                continue
            elif (len(team_p[x[0]]) < 11) or (len(team_p[x[1]]) < 11):
                print("the game can not be held due to loss of the players")
                continue
            else:
                x0 = 0
                for index,i in enumerate(team_p[x[0]]):
                    if index < 11:
                        x0 = players[i][2] + players[i][3] + x0
                    else:
                        break
                
                x1 = 0
                for index,i in enumerate(team_p[x[1]]):
                    if index < 11:
                        x1 = players[i][2] + players[i][4] + x1
                    else:
                        break
                
                if x0 > x1:
                    teams_e[x[0]][0] = teams_e[x[0]][0] + 1
                    teams_e[x[1]][1] = teams_e[x[1]][1] - 1
                    teams[x[0]][1] = teams[x[0]][1] + 1000
                    continue
                elif x0 < x1:
                    teams_e[x[0]][1] = teams_e[x[0]][1] - 1
                    teams_e[x[1]][0] = teams_e[x[1]][0] + 1
                    teams[x[1]][1] = teams[x[0]][1] + 1000
                    continue
                else:
                    continue
        

        x = re.findall('rank', com)
        if x != []:
            all = []
            for i in teams_e:
                all.append(teams_e[i])
            all.sort(reverse=True)
            coun = 1
            for i in all:
                print("{}. {}".format(coun, teams[abs(i[2])][0]))
                coun += 1




# print(players,end="\n\n\n")
# print(teams,end="\n\n\n")
# print(team_p,end="\n\n\n")
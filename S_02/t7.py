che = []
def has_num(a = str):
    global che
    def inner(b):
        if a.isalpha():
            print(f"{b} should have at least one number!")
            che.append(1)
    return inner

def has_uppercase(a):
    global che
    taf = a.lower()
    def inner(b):
        if taf == a:
            print(f"{b} should have at least one capital letter!")
            che.append(1)
    return inner

def has_lowercase(a):
    global che
    taf = a.upper()
    def inner(b):
        if taf == a:
            print(f"{b} should have at least one lowercase letter!")
            che.append(1)
    return inner

def length_bigger_than_8(a):
    global che
    def inner(b):
        if len(a) < 8:
            print(f"{b} have to be at least 8 characters!")
            che.append(1)
    return inner

# @length_bigger_than_8
# @has_lowercase
# @has_uppercase
# @has_num
def validation_username(usernamee):
    global che
    fuc = length_bigger_than_8(usernamee)
    fuc("username")
    fuc = has_uppercase(usernamee)
    fuc("username")
    fuc = has_lowercase(usernamee)
    fuc("username")
    fuc = has_num(usernamee)
    fuc("username")
    if che == []:
        return "1"
    else:
        che.clear()
        return "0"

# @length_bigger_than_8
# @has_lowercase
# @has_uppercase
# @has_num
def validation_password(passw):
    global che
    fuc = length_bigger_than_8(passw)
    fuc("password")
    fuc = has_uppercase(passw)
    fuc("password")
    fuc = has_lowercase(passw)
    fuc("password")
    fuc = has_num(passw)
    fuc("password")
    # print(che)
    if che == []:
        return "1"
    else:
        che.clear()
        return "0"

all_user = {}
co = 0
while True:
    comman = input()

    if comman == "exit":
        break
    
    comman = comman.split(" ")


    if comman[0] == "Sign":
        co += 1
        anw = list(zip(validation_username(comman[2]), validation_password(comman[3])))
        # print(anw)
        if anw[0] == ["1", "1"]:
            print(f"{comman[2]} signed up successfully!")
            if comman[2] in all_user:
                if type(all_user[comman[2]]) == list:
                    all_user[2] = [*all_user[2], comman[3]]
                else:
                    all_user[2] = [all_user[2], comman[3]]
            else:   
                all_user[comman[2]] = comman[3]
        
        # print(che)

    else:
        if all_user == {}:
            print("you should sign up first!")
        else:
            if comman[2] in all_user:
                if type(all_user[comman[2]]) == list:
                    if comman[3] in all_user[comman[2]]:
                        print(f"{comman[2]} logged in successfully!")
                    else:
                        print("username or password is not correct!")
                else:
                    if all_user[comman[2]] == comman[3]:
                        print(f"{comman[2]} logged in successfully!")
                    else:
                        print("username or password is not correct!")
            else:
                if comman[3] in all_user.values():
                    print("username or password is not correct!")
                else:
                    print("you should sign up first!")
                

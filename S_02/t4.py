words = None
counter1 = 0
def memorize(**args):
    global words, counter1

    if words != None:
        for i in words:
            print(f"{i}: {words[i]}")
    else:
        print(words)
    print()

    def emal():
        global words, counter1
        d = []
        w = []
        for i in args:
            d.append(i)
        d.sort()
        for i in d:
            w.append(args[i].split(", "))
        for i in w:
            i.sort()
            i.sort(key=len)
        words = {}
        for index,i in enumerate(d):
            words[i] = ", ".join(w[index])
        counter1 += len(d)

    if len(args) != 0:
        return emal()
    else:
        words = None

try:
    if __name__ == '__main__':
        while counter1 < 504:
            exec(input().replace('\\n', '\n'))
except:
    pass

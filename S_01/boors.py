
PriceBuy = int(input())
PriceCurrent = int(input())
Count = int(input())
if PriceBuy % 10 != 0 or PriceCurrent % 10 != 0:
    print("Invalid Input")
else:
    a = (PriceCurrent*Count) - (PriceBuy*Count)
    b = a * 100 / (PriceBuy*Count)

    if a >= 0:
        print("Profit")
        print(f'{b:.2f}')
        if (PriceCurrent * Count) > 5000000 and b > 20:
            print("Lucky")
        elif b == 0:
            pass
        else:
            print("Normal")
    else:
        print("Loss")
        print(f'{b:.2f}')
        if ((PriceBuy*Count)-(PriceCurrent*Count)) < -10000000 and b > -20:
            print("Chance")
        else:
            print("under the coverage")


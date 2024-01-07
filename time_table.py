def Time_table(a):
    if a <= 17/100:
        print("15s")
        if 17/100 < a <= 33/100:
            print("20")
            if 33/100 < a <= 50/100:
                print("30s")
                if 50/100 < a <= 67/100:
                    print("40")
                    if 67/100 < a <= 83/100:
                        print("50")
                    else:
                        print("60")

Time_table(25)
for i in range(int(input())):
    x = int(input())
    if x == 0:
        print("NULL")
    else:
        if x % 2:
            print("ODD", end=" ")
        else:
            print("EVEN", end=" ")
        if x > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")

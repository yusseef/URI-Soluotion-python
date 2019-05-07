base = 1
for i in range(int(input())):
    list = []
    for j in range(3):
        list.append(base + j)
    base += 4
    print(" ".join(map(str, list)), "PUM")

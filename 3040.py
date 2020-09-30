x = int(input())

for i in range(x):
    height, diameter, branches = input().split()
    height = int(height)
    diameter = int(diameter)
    branches = int(branches)
    if height >= 200 and height <= 300 and diameter >= 50 and branches >= 150:
        print("Sim")
    else:
        print("Nao")

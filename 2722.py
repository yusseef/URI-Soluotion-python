n = int(input())
while n:
    n -= 1
    p1 = input()
    p2 = input()
    name = ''
    for d in range(0, len(p1) - 1, 2):
        name += p1[d:d+2] + p2[d:d+2]
    print(name)

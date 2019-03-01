start, end = map(int, input().split())
if start >= end:
    print("O JOGO DUROU {} HORA(S)".format(abs(start - 24) + end))
else:
    print("O JOGO DUROU {} HORA(S)".format(end - start))

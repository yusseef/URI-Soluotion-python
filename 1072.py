x = int(input())
incou = 0
outcou = 0
for i in range(x):
    n = int(input())
    if n >= 10 and n <= 20:
        incou += 1
    else:
        outcou +=1
print(incou,'in')
print(outcou,'out')


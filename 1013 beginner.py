a, b, c = input().split(" ")
a=int(a)
b=int(b)
c=int(c)
maior = (a + b + abs(a - b))/ 2
result = (maior + c + abs(maior -c))/2
print("%d eh o maior"%result)


a=int(input())
b=int(input())
result=0
for n in range((b+1),a):
    if (n%2!=0):
        result+=n
print(result)

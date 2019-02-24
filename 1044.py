numbers=input().split()
a=int(numbers[0])
b=int(numbers[1])
if a%b==0 or b%a==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

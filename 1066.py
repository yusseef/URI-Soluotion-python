from array import *
numbers=array('i',[])
for i in range(5):
    x=int(input())
    numbers.append(x)
even=0
odd=0
neg=0
pos=0
for e in numbers:
    if e%2==0 or e==0:
        even+=1
print(even,"valor(es) par(es)")
for e in numbers:
    if e%2!=0:
        odd+=1
print(odd,"valor(es) impar(es)")
for e in numbers:
    if e>0:
        pos+=1
print(pos,"valor(es) positivo(s)")
for e in numbers:
    if e<0:
        neg+=1
print(neg,"valor(es) negativo(s)")

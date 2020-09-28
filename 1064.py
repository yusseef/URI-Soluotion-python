count=0
sum=0.0
for i in range(6):
    n = float(input())
    if(n>0):
        sum = sum + n
        count=count+1
print("{} valores positivos".format(count))
print("%0.1f"%(sum/count))

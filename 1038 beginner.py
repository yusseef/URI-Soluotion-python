a,b=input().split(" ")
a=int(a)
b=int(b)
if a==1:
	result=4*b
elif a==2:
	result=4.50*b
elif a==3:
	result=5*b
elif a==4:
	result=2*b
elif a==5:
	result=1.50*b
print("Total: R$ %.2f"%result)

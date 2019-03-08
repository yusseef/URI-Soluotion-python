x=float(input())
if x>=0 and x<=400.00:
    increase = x*(15/100)
    salary = x+increase
    precent = "15"
elif x>=400.01 and x<=800.00:
    increase = x*(12/100)
    salary = x+increase
    precent = "12"
elif x>=800.01 and x<=1200.00:
    increase = x*(10/100)
    salary = x+increase
    precent = "10"
elif x>=1200.01 and x<=2000.00:
    increase = x*(7/100)
    salary = x+increase
    precent = "7"
elif x>2000.0:
    increase = x*(4/100)
    salary=x+increase
    precent="4"

print("Novo salario: %.2f"%salary)
print("Reajuste ganho: %.2f"%increase)
print("Em percentual:", precent,"%")

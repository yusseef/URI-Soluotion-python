code1,amount1,price1=input().split()
code2,amount2,price2=input().split()
code1=int(code1)
amount1=int(amount1)
price1=float(price1)
code2=int(code2)
amount2=int(amount2)
price2=float(price2)
total1=amount1*price1
total2=amount2*price2
TOTAL=total1+total2
print("VALOR A PAGAR: R$ %.2f"%TOTAL)

salary = float(input())

if(salary> 0 and salary <= 2000):
 print ("Isento")
elif(salary > 2000 and salary <= 3000):
 rest = salary - 2000
 result = rest * 0.08
 print ("R$ %.2f"%result)
elif(salary > 3000 and salary < 4500):
 rest = salary - 3000
 result = (rest * 0.18) + (1000 * 0.08)
 print ("R$ %.2f"%result)
else:
 rest = salary - 4500
 result = (rest * 0.28) + (1500 * 0.18) + (1000 * 0.08)
 print ("R$ %.2f"%result)

import math
a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
try:
    x1 = ((-b) + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
    x2 = ((-b) - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
    print("R1 = %.5f"%x1)
    print("R2 = %.5f"%x2)
except ValueError:
    print("Impossivel calcular")
except ZeroDivisionError:
    print("Impossivel calcular")

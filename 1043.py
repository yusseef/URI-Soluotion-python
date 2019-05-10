data = input().split()
all_data = sorted(map(float, data))
value1 = all_data[2]
value2 = all_data[1]
value3 = all_data[0]
if value1 >= value2 + value3:
    print("Area =", format((float(data[0]) + float(data[1])) * float(data[2]) / 2, ".1f"))
else:
    print("Perimetro =", format((value1 + value2 + value3), ".1f"))

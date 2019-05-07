num1, num2, counter = int(input()), int(input()), 0
while num2 <= num1:
    num2 = int(input())
total = num1
while total < num2:
    total += num1 + counter
    counter += 1
if num2 <= 0:
    print(counter)
else:
    print(counter + 1)

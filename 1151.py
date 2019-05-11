first, second, list, loops = 0, 1, ["0", "1"], int(input())
if loops == 1:
    print("0")
elif loops == 2:
    print("0 1")
else:
    for i in range(loops - 2):
        list.append(first + second)
        first, second = second, first + second
print(" ".join(map(str, list)))

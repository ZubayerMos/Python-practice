list = [10, 15, 22, 32, 35, 40, 43, 50, 52, 70, 75, 80]
length = len(list)
i = 0
while i < length:
    if list[i] % 5 == 0:
        list[i] = 0
    i += 1
print(list)
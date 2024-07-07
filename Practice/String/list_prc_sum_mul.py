list = [10,15,20,25,50,55,60]
sum = 0
mul = 1
for i in range (len(list)):
    sum = sum + list[i]
    mul = sum *mul
print (sum)
print (mul)

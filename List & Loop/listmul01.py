list = [5,17,12,8,6,3,7,13]
for i in range (0, len(list)):
    if list[i]%2==0:
        num = list[i]*3
    else:
        num = list[i]*4
    list[i] = num
print(list)
    
    
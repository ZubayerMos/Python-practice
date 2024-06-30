list = [12,17,11,9,5,14,24,8]
minimum = 99999999999999
for i in range (len(list)):
    if list[i]<minimum:
        minimum = list[i]
print (minimum)
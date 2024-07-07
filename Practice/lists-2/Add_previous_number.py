list = [12,10,15,10,25,27]
prev_number = 0
for i in range (len(list)):
    temp = list[i]
    list [i]=prev_number+ list[i]
    prev_number= temp
    
print (list)

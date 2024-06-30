list = [5,6,7,6,6,8,6,5,3,8]
min_cnt = 100000
min_number = 1000000
for i in range (len(list)):
    count = 0
    for j in range (len(list)):
        if list[i]== list[j]:
            count +=1
    if count<min_cnt :
        min_cnt = count 
        min_number= list[i]
print (f"The {min_number} has appeared by",min_cnt)
    


list = [5,6,7,6,6,8,6,5,3,8]
max_cnt = 0
most_number = 0
for i in range (len(list)):
    count = 0
    for j in range (len(list)):
        if list[i]==list[j]:
            count +=1
    if count > max_cnt :
        max_cnt = count
        most_number = list[i]
        
print (f"The number has appeared for most number timees",most_number )
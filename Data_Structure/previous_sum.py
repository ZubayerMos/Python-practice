list = [10,12,15,18,20]
previous_number = 0
for i in range (len(list)):
    temp_numb = list [i]
    list [i]= previous_number+ list[i]
    previous_number= temp_numb
print (list)
    

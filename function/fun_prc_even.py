def even_number(list):
    even_list = []
    for i in range(len(list)):
        if (list[i]%2==0):
            even_list.append(list[i])
    return even_list            
list = [5,10,12,20,24,25,30]
print (even_number(list))


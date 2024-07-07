list = [5,4,10,12,16,8]

temp = list[0]
list[0] = list[len(list)-1]
list[len(list)-1] = temp 

print(list)
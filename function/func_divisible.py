def list_of_divisible(list):
    cnt = 0
    for i in range (len(list)):
        if list[i]%5==0:
            cnt+=1
    return cnt
list1 =[5,15,25,20,21,10,12,7]
print (list_of_divisible(list1))
        
        
        
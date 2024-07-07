num_list = [20,10,5,3,7,10]
num_of_evens = 0
for i in range (0,(len(num_list))):
    if (num_list[i]%2==0):
        num_of_evens = num_of_evens + 1
        print("The even number is", num_list[i])
        
print ("The number of evens is :", num_of_evens)
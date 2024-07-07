list1= [5,9,12,13,14,2,9]
countdivisibleby5 = 0
for i in range (0,(len(list1))):
    if (list1[i]%5==0):
        countdivisibleby5 = countdivisibleby5 + 1
        
print ("List1 divisible by 5 total numbers : ",countdivisibleby5)
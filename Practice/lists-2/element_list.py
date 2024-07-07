list1 = [5,9,12,13,14,2,9]
countlessthan10 = 0
countmorethan10 = 0
for i in range(0,len(list1)):
    if list1[i]<=10:
        countlessthan10=countlessthan10+1
    else:
        countmorethan10=countmorethan10+1

print("The number <10 is",countlessthan10 )
print("The number >10 is",countmorethan10 )
list = [5,6,2,3,4,8,9,12,5]
even = 0
sum_of_even =0
odd = 0
sum_of_odd = 0
for i in range (len(list)):
    if list[i]%2==0 :
        sum_of_even = sum_of_even + list[i]
    else:
        sum_of_odd = sum_of_odd + list[i]
if (sum_of_even>sum_of_odd):
    print ("sum_of_even is a large number")
else :
    print ("Sum_of_odd is a small number ")



       
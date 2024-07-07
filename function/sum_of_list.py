def sum_of_list(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    return sum 

list = [5,8,7,10,15,20,2]

print(sum_of_list(list))
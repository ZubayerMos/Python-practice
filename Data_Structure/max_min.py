list = [15,20,25,30,35,40,45,50,55,60]
max = 0
min = 100
for i in range (len(list)):
    if (list[i]>max):
        max = list[i]
    if (list[i]<min):
        min = list[i]
print (max)
print (min)
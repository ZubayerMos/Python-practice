sentence = 'I love Bangladesh bank'
cnt = 0
for i in range (len(sentence)):
    if sentence[i].lower() == 'a' or sentence[i].lower() == 'e' or sentence[i].lower() == 'i' or sentence[i].lower() == 'o' or sentence[i].lower() == 'u':
        cnt = cnt+1
print ("number of vowles",cnt)


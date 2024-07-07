sentence = 'I love to play cricket.'
cnt = 0
for i in  range (len(sentence)):
    if sentence[i] ==' ':
        cnt = cnt + 1
print (f"Total number of word is {cnt+1}")
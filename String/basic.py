sentence = 'I love Bangladesh bank'
cnt = 0
for i in range(len(sentence)):
    if sentence[i].lower()=='b':
       cnt = cnt + 1
print(cnt)
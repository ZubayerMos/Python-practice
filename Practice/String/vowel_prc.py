file = "I Love to play cricket"
cnt = 0
consonant = 0
for i in range (len(file)):
    if (file[i].upper()== "A" or file[i].upper()=="E" or file[i].upper()=="I" or file[i].upper()=="O" or file[i].upper()=="U"):
        cnt = cnt+1
    else :
        if file[i]!= ' ':
            consonant=consonant+1
        

print ("number of vowels",cnt)
print ("number of consonant", consonant)

mystring = "This is an another file."
num_of_vowel = 0
num_of_cnstnt=0
for i in range (len(mystring)):
    
   # if (mystring[i].lower()== "a" or mystring[i].lower()=="e" or mystring[i].lower()=="i" or mystring[i].lower()=="o"or mystring[i].lower()=="u"):
        #num_of_vowel = num_of_vowel+1
#print (num_of_vowel)
   if (mystring[i].upper()=="A" or mystring[i].upper()=="E" or mystring[i].upper()=="I"or mystring[i].upper()=="O" or mystring[i].upper()=="U"):
       num_of_vowel = num_of_vowel+1
   elif mystring[i]== " " or mystring[i]== "." or mystring[i]=="," or mystring[i]==";":
       continue
   else:
       num_of_cnstnt= num_of_cnstnt+1
       
print (num_of_vowel)
print (num_of_cnstnt)
    

        
        
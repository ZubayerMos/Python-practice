my_string= "This is Rakib file"
cnt = 0
for i in range (len(my_string)):
    if my_string[i].lower() == "a" or my_string[i].lower()=="e" or my_string[i].lower()=="i" or my_string[i].lower()=="o" or my_string[i].lower()=="u":
        cnt= cnt+1
print ("number of vowels", cnt)
    
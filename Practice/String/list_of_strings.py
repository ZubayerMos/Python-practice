# Let's assume all the girls have a in their last letter of the name
list = ['Rafiqa', 'Sarifa', 'Imtiaj', 'Arifa', 'Shekh', 'Tafsir', 'Sadik']
cnt_female = 0
for i in range(len(list)):
    if (list[i][-1] =='a' ):
        print(f"{list[i]} is a girls name")
for i in range (len(list)):
    cnt_vowels = 0
    for j in range(len(list[i])):
        if list[i][j].lower()=="a" or list[i][j].lower()=="e" or list[i][j].lower()=="i" or list[i][j].lower()=="o" or list[i][j].lower()=="u": 
            cnt_vowels= cnt_vowels+1
    print (f"number of vowels in word {list[i]} is :", cnt_vowels) 
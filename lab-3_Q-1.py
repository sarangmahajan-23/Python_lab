str = input("Enter your string : ")

char_ct = {}

for ch in str:
    if ch in char_ct:
        char_ct[ch]+=1
    else:
        char_ct[ch]=1

print(char_ct)
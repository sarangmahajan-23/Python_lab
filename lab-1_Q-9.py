s1 = input("Enter your string : ")
l1 = list(s1)
n = len(s1)
l1[0],l1[n-1]=l1[n-1],l1[0]

s2 = "".join(l1)
print("The new string is :",s2)
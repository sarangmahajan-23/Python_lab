a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3rd number : "))
d = 0
if (b>c ):
    if(b>a):
        d = b
if (a>c ):
    if(a>b):
        d = a
if (c>a ):
    if(c>b):
        d = c

print("The largest number is : ",d)